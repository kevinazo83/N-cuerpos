#include <iostream>
#include <fstream>
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
		std::vector<double> x{0,0,0}, v{0,0,0},F{0,0,0}, A{0,0,0};  //se agregaron los vectores fuerza y aceleracion,

		//Inicializar el cuerpo
		void init(double m0, double x0, double y0, double z0, double vx0, double vy0, double vz0,double Fx0, double Fy0, double Fz0 ,double Ax0, double Ay0, double Az0 );
		//Imprime la posición del cuerpo
		void print();

};

void cuerpo::init(double m0, double x0, double y0, double z0, double vx0, double vy0, double vz0,double Fx0, double Fy0, double Fz0,double Ax0, double Ay0, double Az0){
	m = m0;
	x.at(0) = x0;
	x.at(1) = y0;
	x.at(2) = z0;
	v.at(0) = vx0;
	v.at(1) = vy0;
	v.at(2) = vz0;
    F.at(0) = Fx0;
	F.at(1) = Fy0;
	F.at(2) = Fz0;
    A.at(0) = Ax0;
	A.at(1) = Ay0;
	A.at(2) = Az0;

}

void cuerpo::print(){
	std::cout<< x.at(0) << "\t\t" << x.at(1) << "\t\t" << x.at(2)<<"\n";
}

//Operaciones con cuerpos
//Calcula la fuerza de dos cuerpos al intractuar gravitacionalmente y actualiza sus velocidades ( a1 = Gm2r/|r|^3 )
    void NewF(cuerpo&a, cuerpo&b);

	//Hace la fuerza neta sobre un cuerpo igual a cero antes de empezar una iteracion
	void limpF(cuerpo &a);

	//Actualiza la posición de un cuerpo
    void Tstep(cuerpo &a);

    void Vstep(cuerpo &a);

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

	//Soldouble vx0, double vy0, double vz0
	M = 332959;
	V = 0;
	X = 0;
	Sol.init(M,X,0,0,0,V,0,0,0,0,0,0,0);

	//Mercurio
	M = 0.0553;
	V = 1.036156924;
	X = 0.3074916;
	Mer.init(M,X,0,0,0,V,0,0,0,0,0,0,0);

	//Venus
	M = 0.815;
	V = -0.6152291537;
	X = -0.6194454586;
	Ven.init(M,X,0,0,0,V,0,0,0,0,0,0,0);

	//Tierra
	M = 1;
	V = 0.5321328117;
	X = 0.975949724;
	Tie.init(M,X,0,0,0,V,0,0,0,0,0,0,0);

	//Marte
	M = 0.1074;
	V = -0.4655503305;
	X = -1.38137259;
	Mar.init(M,X,0,0,0,V,0,0,0,0,0,0,0);

	//Jupiter
	M = 317.833;
	V = 0.2410320956;
	X = 4.950581337;
	Jup.init(M,X,0,0,0,V,0,0,0,0,0,0,0);

	//Saturno
	M = 95.152;
	V = -0.1788415987;
	X = -9.074705468;
	Sat.init(M,X,0,0,0,V,0,0,0,0,0,0,0);

	//Urano
	M = 14.536;
	V = 0.1249080321;
	X = 18.26697968;
	Ura.init(M,X,0,0,0,V,0,0,0,0,0,0,0);

	//Neptuno
	M = 17.147;
	V = -0.0966236535;
	X = -29.88718083;
	Nep.init(M,X,0,0,0,V,0,0,0,0,0,0,0);

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

    std::ofstream outfile;
    outfile.open("datos.txt");
	//Ciclo para N-1 pasos de tiempo (imprime N valores para cada cuerpo)
	for (int i = 0; i <= N; i++){

         for (int j = 0; j < Sistema.size(); j++){
             Tstep(Sistema.at(j));
             //Sistema.at(j).print();
			 outfile<< Sistema.at(j).x.at(0) << "\t\t" << Sistema.at(j).x.at(1) << "\t\t" << Sistema.at(j).x.at(2)<<"\n";

         }
         for (int j = 0; j < Sistema.size(); j++){
             limpF(Sistema.at(j));
             //Sistema.at(j).print();
         }
		//Interacion entre todos los cuerpos del sistema
		 for (int j = 0; j < Sistema.size()-1; j++){
             for (int k = 0; k < Sistema.size()-1; k++){
                 if (j!=k){
                     	NewF(Sistema.at(j),Sistema.at(k));
                 }
			}
		}

		//Imprime y actualiza los cuerpos
		 for (int j = 0; j < Sistema.size(); j++){
             Vstep(Sistema.at(j));
		 }
		 outfile<<std::endl;
	}
    outfile.close();
	return 0;
}
void limpF(cuerpo&a){  //funcion para hacer la fuerza total sobre un cuerpo igual a cero, al iniciar una nueva iteracion

	a.F.at(0) =0 ;
	a.F.at(1) =0;
	a.F.at(2) =0;
}

void NewF(cuerpo &a, cuerpo &b){       //calcula la fuerza que ejerce el cuerpo b sobre el cuerpo a, Jack calculaba la aceleración, lo cambie para poder implementar mejor lp

	std::vector<double> R{0,0,0};
	double r = 0;

	// Distancia entre los dos cuerpos
	for (int i=0; i <= 2; i++){

		R.at(i) = (a.x.at(i)-b.x.at(i));
		r += pow(R.at(i),2);
	}
	r = sqrt(r);

	double r3 = pow(r,3);
	double G = 80.79*pow(10,-8);
    //double G = 1200;
	// Aceleraciones de los cuerpos
	// F = -Gm1m2/|r|^3 * r y F = ma
	double Fa = -G*b.m*a.m/r3;
	double Fb = -G*a.m*b.m/r3;


	a.F.at(0) += Fa*R.at(0)*1;
	a.F.at(1) += Fa*R.at(1)*1;
	a.F.at(2) += Fa*R.at(2)*1;



}




void Vstep(cuerpo &a){   //algoritmo lp para la aceleracion y velocidad

    std::vector<double> An{0,0,0};
    An.at(0) = a.F.at(0)/a.m;
    An.at(1) = a.F.at(1)/a.m;
    An.at(2) = a.F.at(2)/a.m;

    a.v.at(0) += 0.5*(a.A.at(0)+An.at(0))*dt;
    a.v.at(1) += 0.5*(a.A.at(1)+An.at(1))*dt;
    a.v.at(2) += 0.5*(a.A.at(2)+An.at(2))*dt;

    a.A.at(0) = An.at(0) ;
    a.A.at(1) =  An.at(1);
    a.A.at(2) =  An.at(2);

}
void Tstep(cuerpo &a){         //algoritmo lp para el siguiente paso en la posicion

	a.x.at(0) += a.v.at(0)*dt+0.5*a.A.at(0)*pow(dt,2);
	a.x.at(1) += a.v.at(1)*dt+0.5*a.A.at(1)*pow(dt,2);
	a.x.at(2) += a.v.at(2)*dt+0.5*a.A.at(2)*pow(dt,2);

}
