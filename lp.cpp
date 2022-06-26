#include <cstdlib>
#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <string>
#include <stdlib.h>
//#include<conio.h>


// Unidades:
// Masa = Masa terrestre, Distancia = U.astronómica, tiempo = mes.

// Variables globales

	double N = 3000; // Numero de pasos que se imprimen para cada planeta
	double dt = 0.01; // ª
	int cont = 0; // Contador para ver en que iteración se está
	int imp = 100; // Cada cuantos dt se imprimen datos

		//Nota: hice más pequeño dt para ver si mercurio mejoraba y se redujo el # de datos al imprimir cada 100 pasos. El tiempo total transcurrido es el mismo que antes.

// Si tomamos dt = 0.5 (Medio mes), mercurio no matiene su orbita.
// Si tomamos dt = 0.15 (Cuatro dias y medio), la orbita de mercurio choca con la de venus.

// Clase para cada cuerpo
class cuerpo {

	public:

		// Cada cuerpo tiene masa, posición, velocidad, aceleración y fuerza.
		double m;
		std::vector<double> x{0,0,0}, v{0,0,0}, A{0,0,0}, F{0,0,0};

		// Función para inicializar el cuerpo
		void init(double m0, double x0, double y0, double z0, double vx0, double vy0, double vz0,double Fx0, double Fy0, double Fz0 ,double Ax0, double Ay0, double Az0 );
			
		// Función para imprimir la posición del cuerpo (Creo que se puede eliminar al usar outfile)
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

// Operaciones con cuerpos

	// Calcula la fuerza que ejerce b sobre a y actualiza la fuerza sobre a
    void NewF(cuerpo&a, cuerpo&b);

	// Hace igual a cero la fuerza neta sobre un cuerpo antes de empezar una iteracion
	void limpF(cuerpo &a);

	// Algoritmo lp para la aceleracion y velocidad
    void Vstep(cuerpo &a);

	// Algoritmo lp para el siguiente paso en la posicion
    void Tstep(cuerpo &a);


// Función main
int main(){

	//En este vector almacenamos todos los cuerpos del sistema
	std::vector<cuerpo>Sistema;
    std::vector<float>vNotas;


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
    float cal = 0; //nosequesesto

	// Insertar descripción
    std::ifstream fNotas ("entrada.txt"); //Apertura del archivo en modo lectura
    if(fNotas.is_open()){


         while (fNotas >> cal){
                vNotas.push_back(cal);
         }
    float l=vNotas[vNotas.size()-1];
    std::vector<std::vector<float>>ordenando(l);
    std::vector<std::vector<cuerpo>>ordenando1(l);
    for (int k = 0; k < l; k++){
        for (int m=0; m < 13;m++){
            ordenando[k].push_back(vNotas[(k*13)+m]);

        }
    }
    cuerpo C;
    for (int k = 0; k < l; k++){
           //cuerpo ordenando1[k].init=ordenando[k];
        //for (int m=0; m < 13;m++){
            C.init(ordenando[k][0],ordenando[k][1],ordenando[k][2],ordenando[k][3],ordenando[k][4],ordenando[k][5],ordenando[k][6],ordenando[k][7],ordenando[k][8],ordenando[k][9],ordenando[k][10],ordenando[k][11],ordenando[k][12]);
            Sistema.push_back(C);
        }
        //std::cout <<"\n";
        //std::cout<<std::endl;
    }
    //std::cout<<std::endl;

    
    fNotas.close();




    std::ofstream outfile;
    outfile.open("datos.txt");
	
	// Ciclo para pasos de tiempo (Como se imprime cada 'imp' pasos, se imprime N valores para cada cuerpo)
	for (int i = 0; i <= N*imp; i++){

        for (int j = 0; j < Sistema.size(); j++){

			// Inicializa?
            Tstep(Sistema.at(j));

			// Imprime valores cada 'imp' pasos
			if (cont%imp == 0){
				outfile<< Sistema.at(j).x.at(0) << "\t\t" << Sistema.at(j).x.at(1) << "\t\t" << Sistema.at(j).x.at(2)<<"\n";
			}
        }

		// Limpia las fuerzas para calcularlas en este tiempo
        for (int j = 0; j < Sistema.size(); j++){
            limpF(Sistema.at(j));
        }
		
		// Interacion entre todos los cuerpos del sistema 
		for (int j = 0; j < Sistema.size(); j++){
            for (int k = 0; k < Sistema.size(); k++){
                if (j!=k){
                    NewF(Sistema.at(j),Sistema.at(k));
                }
			}
		}

		// Actualiza aceleración y velocidad de los cuerpos
		for (int j = 0; j < Sistema.size(); j++){
            Vstep(Sistema.at(j));
		}
		outfile<<std::endl; //nosequehace
		cont += 1; // Actualiza el contador de pasos
		
	}
    outfile.close();  //nosequehace
	return 0;
}

// Funcion para hacer la fuerza total sobre un cuerpo igual a cero al iniciar una nueva iteracion
void limpF(cuerpo &a){

	a.F.at(0) =0 ;
	a.F.at(1) =0;
	a.F.at(2) =0;
	
}

// Calcula la fuerza que ejerce el cuerpo b sobre el cuerpo a
void NewF(cuerpo &a, cuerpo &b){

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
	
	// F = -Gm1m2/|r|^3 * r
	double Fa = -G*b.m*a.m/r3;

	a.F.at(0) += Fa*R.at(0)*1;
	a.F.at(1) += Fa*R.at(1)*1;
	a.F.at(2) += Fa*R.at(2)*1;
	
}

// Algoritmo lp para la aceleracion y velocidad
void Vstep(cuerpo &a){

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

// Algoritmo lp para el siguiente paso en la posicion
void Tstep(cuerpo &a){

	a.x.at(0) += a.v.at(0)*dt+0.5*a.A.at(0)*pow(dt,2);
	a.x.at(1) += a.v.at(1)*dt+0.5*a.A.at(1)*pow(dt,2);
	a.x.at(2) += a.v.at(2)*dt+0.5*a.A.at(2)*pow(dt,2);

}
