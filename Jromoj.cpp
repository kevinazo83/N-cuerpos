#include <iostream>
#include <vector>
#include <cmath>

/*
actualmente solo se imprime la posición del cuerpo seleccionado (Lineas 138 y 156). Sistema(0) es el sol y los siguientes dependen del orden en el que agregamos los cuerpos.
*/

// Unidades:
// Masa = Masa terrestre, Distancia = U.astronómica, tiempo = mes.

//Variables globales
double dt = 0.5; // medio mes

//Clase para cada cuerpo 
class cuerpo {

	public:
		double m;
		std::vector<double> x{0,0,0}, v{0,0,0};

		//Inicializar el cuerpo
		void init(double m0, double x0, double y0, double z0, double vx0, double vy0, double vz0);
		//Imprime la posición del cuerpo
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

	//Calcula la aceleración de dos cuerpos al intractuar gravitacionalmente y actualiza sus velocidades ( a1 = Gm2r/|r|^3 ) ( Vnew = V0 + dt*a1 )
	void NewV(cuerpo &a, cuerpo &b);

	//Actualiza la posición de un cuerpo ( Xnew = X0 + dt*Vx )
	void Tstep(cuerpo &a);
	
int main(){

	//En este vector almacenamos todos los cuerpos del sistema
	std::vector<cuerpo>Sistema;

	//Cuerpos del sistema solar
	cuerpo Sol;
	cuerpo Mer;
	cuerpo Ven;
	cuerpo Tie;
	cuerpo Mar;
	cuerpo Jup;
	cuerpo Sat;
	cuerpo Ura;
	cuerpo Nep;

	double M = 0;
	double V = 0;
	double X = 0;

	//Inicialización de los cuerpos
	
	//Sol
	M = 332946;
	V = 0;
	X = 0;
	Sol.init(M,X,0,0,0,V,0);

	//Mercurio
	M = 0.055;
	V = 0;
	X = 0.39;
	Mer.init(M,X,0,0,0,V,0);
	
	//Venus
	M = 0.815;
	V = 0.608289;
	X = -0.72;
	Ven.init(M,X,0,0,0,V,0);
	
	//Tierra
	M = 1;
	V = 0.5179144;
	X = 1;
	Tie.init(M,X,0,0,0,V,0);
	
	//Marte
	M = 0.107;
	V = -0.419; //0.41845
	X = -1.52;
	Mar.init(M,X,0,0,0,V,0);
	
	//Jupiter
	M = 317.8;
	V = 0.22715;
	X = 5.2;
	Jup.init(M,X,0,0,0,V,0);

	//Saturno
	M = 95.16;
	V = 0;
	X = 9.54;
	Sat.init(M,X,0,0,0,V,0);

	//Urano
	M = 14.54;
	V = 0;
	X = 19.19;
	Ura.init(M,X,0,0,0,V,0);

	//Neptuno
	M = 17.15;
	V = 0;
	X = 30.06;
	Nep.init(M,X,0,0,0,V,0);

	//Agregamos los cuerpos que vamos a modelar
	Sistema.push_back(Sol);
	Sistema.push_back(Ven);
	Sistema.push_back(Tie);
	Sistema.push_back(Mar);
	Sistema.push_back(Jup);


	//Ciclo para 400 pasos de tiempo
	for (int i = 1; i <= 400; i++){
		
		Sistema.at(0).print();
		
		//Interacion entre todos los cuerpos del sistema
		for (int j = 0; j < Sistema.size()-1; j++){
			for (int k = j+1; k < Sistema.size(); k++){

				NewV(Sistema.at(j),Sistema.at(k));
				
			}
		}

		//Actualiza los cuerpos
		for (int j = 0; j < Sistema.size(); j++){

			Tstep(Sistema.at(j));
				
		}
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
	double G = 80.486*pow(10,-8);

	// Aceleraciones de los cuerpos
	// F = -Gm1m2/|r|^3 * r y F = ma
	double Aa = -G*b.m/r3;
	double Ab = -G*a.m/r3;

	//Actualizamos la velocidad de los cuerpos v = v0 + a*dt

	a.v.at(0) += Aa*R.at(0)*dt;
	a.v.at(1) += Aa*R.at(1)*dt;
	a.v.at(2) += Aa*R.at(2)*dt;
	
	b.v.at(0) += -Ab*R.at(0)*dt;
	b.v.at(1) += -Ab*R.at(1)*dt;
	b.v.at(2) += -Ab*R.at(2)*dt;
 	
}

void Tstep(cuerpo &a){

	//Actualizamos la posición del cuerpo x = x0 + v*dt
	a.x.at(0) += a.v.at(0)*dt;
	a.x.at(1) += a.v.at(1)*dt;
	a.x.at(2) += a.v.at(2)*dt;

}
