#include <iostream>
#include <vector>
#include <cmath>

//Variables globales
double dt = 3600; //1hora

//Clase para cada cuerpo 
class cuerpo {

	public:
		double m;
		std::vector<double> x{0,0,0}, v{0,0,0};

		//Inicializar el cuerpo
		void init(double m0, double x0, double y0, double z0, double vx0, double vy0, double vz0);
		//Ver que los datos estén bien
		void print();

};

void cuerpo::init(double m0, double x0, double y0, double z0, double vx0, double vy0, double vz0){
	m = m0;
	x.at(0) = x0;
	x.at(1) = y0;
	x.at(2) = z0;
	v.at(0) = vx0;
	v.at(1) = vy0;
	v.at(2) = vz0;
}

void cuerpo::print(){
	std::cout<< x.at(0) << "\t\t" << x.at(1) << "\t\t" << x.at(2) << "\n";
}

//Operaciones con cuerpos

	//Calcula la nueva velocidad de los 2 cuerpos ( a1 = Gm2r/|r|^3 ) ( Vnew = V0 + dt*a1 )
	void NewV(cuerpo &a, cuerpo &b);

	//Modifica la posición de los cuerpos ( Xnew = X0 + dt*Vx )
	void Tstep(cuerpo &a);
	
int main(){

	std::vector<cuerpo>Sistema;
	
	cuerpo Sol;
	cuerpo c1;
	cuerpo c2;

	double Msol = 1.989*pow(10,30);

	//Tierra
	double Mt = 5.972*pow(10,24);
	double Vt = 29780;
	double Xt = 150*pow(10,9);

	//Marte
	double Mm = 6.39*pow(10,23);
	double Vm = -24130;
	double Xm = -228*pow(10,9);
	
	Sol.init(Msol,0,0,0,0,0,0);
	c1.init(Mt,Xt,0,0,0,Vt,0);
	c2.init(Mm,Xm,0,0,0,Vm,0);
	
	Sistema.push_back(Sol);
	Sistema.push_back(c1);
	Sistema.push_back(c2);

	
	for (int i = 1; i <= 9000; i++){

		Sistema.at(0).print();
		
		//Interaciones entre los cuerpos (Arreglar al agregar marte)
		NewV(Sistema.at(0),Sistema.at(1));
		//NewV(Sistema.at(0),Sistema.at(2));
		//NewV(Sistema.at(1),Sistema.at(2));

		//Actualizar cuerpos
		Tstep(Sistema.at(0));
		Tstep(Sistema.at(1));
		//Tstep(Sistema.at(2));

	}
	Sistema.at(0).print();
	return 0;
}


void NewV(cuerpo &a, cuerpo &b){

	std::vector<double> R{0,0,0};
	double r = 0;

	// Distancia entre los dos cuerpos
	for (int i=0; i <= 2; i++){
		
		R.at(i) = (a.x.at(i)-b.x.at(i));
		r += pow(R.at(i),2);
	}
	r = sqrt(r);

	double r3 = pow(r,3);
	double G = 6.6738*pow(10,-11);

	// F = -Gm1m2/|r|^3 * r y F = ma
	double Aa = -G*b.m/r3;
	double Ab = -G*a.m/r3;

	//Actualizamos la velocidad de los cuerpos v = a*dt

	a.v.at(0) += Aa*R.at(0)*dt;
	a.v.at(1) += Aa*R.at(1)*dt;
	a.v.at(2) += Aa*R.at(2)*dt;
	
	b.v.at(0) += -Ab*R.at(0)*dt;
	b.v.at(1) += -Ab*R.at(1)*dt;
	b.v.at(2) += -Ab*R.at(2)*dt;
 	
}

void Tstep(cuerpo &a){

	//Actualizamos la posición del cuerpo
	a.x.at(0) += a.v.at(0)*dt;
	a.x.at(1) += a.v.at(1)*dt;
	a.x.at(2) += a.v.at(2)*dt;

}
