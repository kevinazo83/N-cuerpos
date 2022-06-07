#include <iostream>
#include <vector>
#include <cmath>
//PROBLEMA TSTEP VELOCIDAD NO SE ACTUALIZA
//Variables globales
double dt = 604800; //Una semana
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
	void NewV(cuerpo a, cuerpo b);

	
int main(){

	std::vector<cuerpo>Sistema;
	
	cuerpo Sol;
	cuerpo c1;

	double Msol = 0.45*pow(10,10);
	double Mc1 = 0.45*pow(10,5);
	double dis = 30;
	
	Sol.init(Msol,0,0,0,0,0,0);
	c1.init(Mc1,dis,0,0,0,0,0);
	Sistema.push_back(Sol);
	Sistema.push_back(c1);

	NewV(Sistema.at(0),Sistema.at(1));
	
	return 0;
}


void NewV(cuerpo a, cuerpo b){

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
	std::cout<< b.v.at(0) << "\n"; //velocidad del cuerpo menos masivo
}
