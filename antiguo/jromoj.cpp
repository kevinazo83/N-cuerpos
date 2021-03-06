#include <iostream>
#include <vector>
#include <cmath>

// Unidades:
// Masa = Masa terrestre, Distancia = U.astronómica, tiempo = mes.

//Variables globales
double N = 10000; // Numero de pasos
double dt = 0.1; // Tres Dias (Mercurio no presenta problemas)
// Si tomamos dt = 0.5 (Medio mes), mercurio no matiene su orbita.
// Si tomamos dt = 0.15 (Cuatro dias y medio), la orbita de mercurio choca con la de venus.

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
	M = 332959;
	V = 0;
	X = 0;
	Sol.init(M,X,0,0,0,V,0);

	//Mercurio
	M = 0.0553;
	V = 1.036156924;
	X = 0.3074916;
	Mer.init(M,X,0,0,0,V,0);
	
	//Venus
	M = 0.815;
	V = -0.6152291537;
	X = -0.6194454586;
	Ven.init(M,X,0,0,0,V,0);
	
	//Tierra
	M = 1;
	V = 0.5321328117;
	X = 0.983271237;
	Tie.init(M,X,0,0,0,V,0);
	
	//Marte
	M = 0.1074;
	V = -0.4655503305;
	X = -1.38137259;
	Mar.init(M,X,0,0,0,V,0);
	
	//Jupiter
	M = 317.833;
	V = 0.2410320956;
	X = 4.950581337;
	Jup.init(M,X,0,0,0,V,0);

	//Saturno
	M = 95.152;
	V = -0.1788415987;
	X = -9.074705468;
	Sat.init(M,X,0,0,0,V,0);

	//Urano
	M = 14.536;
	V = 0.1249080321;
	X = 18.26697968;
	Ura.init(M,X,0,0,0,V,0);

	//Neptuno
	M = 17.147;
	V = -0.0966236535;
	X = -29.88718083;
	Nep.init(M,X,0,0,0,V,0);

	//Agregamos los cuerpos que vamos a modelar
	Sistema.push_back(Sol);
	Sistema.push_back(Mer);
	Sistema.push_back(Ven);
	Sistema.push_back(Tie);
	Sistema.push_back(Mar);
	Sistema.push_back(Jup);
	Sistema.push_back(Sat);
	Sistema.push_back(Ura);
	Sistema.push_back(Nep);


	//Ciclo para N-1 pasos de tiempo (imprime N valores para cada cuerpo)
	for (int i = 1; i <= N; i++){
		
		//Interacion entre todos los cuerpos del sistema
		for (int j = 0; j < Sistema.size()-1; j++){
			for (int k = j+1; k < Sistema.size(); k++){

				NewV(Sistema.at(j),Sistema.at(k));
				
			}
		}

		//Imprime y actualiza los cuerpos
		for (int j = 0; j < Sistema.size(); j++){

			Sistema.at(j).print();
			Tstep(Sistema.at(j));
				
		}
	}
	
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
