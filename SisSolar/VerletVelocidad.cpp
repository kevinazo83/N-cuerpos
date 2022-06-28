#include <cstdlib>
#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <string>
#include<stdlib.h>
//#include<conio.h>

// Unidades:
// Masa = Masa terrestre, Distancia = U.astronómica, tiempo = mes.

//Variables globales
double N = 20000; // Numero de pasos
//double dt = 0.01; // 7.7 horas (Mercurio no presenta problemas)
// Si tomamos dt = 0.5 (Medio mes), mercurio no matiene su orbita.
// Si tomamos dt = 0.15 (Cuatro dias y medio), la orbita de mercurio choca con la de venus.

//Clase para cada cuerpo
class cuerpo {

	public:
		double m;                                                      //masa de cada cuerpo
        double dt;                                                    //dt con el que se calculara la orbita de cada cuerpo
		std::vector<double> x{0,0,0}, v{0,0,0},F{0,0,0}, A{0,0,0};   // vectores posicion, velocidad,  fuerza y aceleracion,

		//Inicializar el cuerpo
		void init(double m0, double x0, double y0, double z0, double vx0, double vy0, double vz0,double Fx0, double Fy0, double Fz0 ,double Ax0, double Ay0, double Az0,double dt0);
		//Imprime la posición del cuerpo
		void print();

};

void cuerpo::init(double m0, double x0, double y0, double z0, double vx0, double vy0, double vz0,double Fx0, double Fy0, double Fz0,double Ax0, double Ay0, double Az0,double dt0){
	m = m0;
    dt=dt0;
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
    //vector donde se almacenan todos los datos de entrada en un vector de una fila
    std::vector<float>datosin;

    float cal = 0;        //se utiliza par extraer las componentes de los dats de entrada

    std::ifstream fentrada ("entrada.txt");   //Apertura del archivo en modo lectura

    //pasando los datos de fentrada(str) a datosin(float)
    if(fentrada.is_open()){
         while (fentrada >> cal){
                datosin.push_back(cal);
         }
    //l es el numero de cuerpos
         float l=datosin[datosin.size()-1];

    //el vector ordenando tendra en las filas los planetas y en las columnas los datos del planeta
    std::vector<std::vector<float>>ordenando(l);
    // pasando los datos a ordenando
    for (int k = 0; k < l; k++){
        for (int m=0; m < 14;m++){
            ordenando[k].push_back(datosin[(k*14)+m]);

        }
    }
    //inicializando los datos
    cuerpo C;
    for (int k = 0; k < l; k++){
            C.init(ordenando[k][0],ordenando[k][1],ordenando[k][2],ordenando[k][3],ordenando[k][4],ordenando[k][5],ordenando[k][6],ordenando[k][7],ordenando[k][8],ordenando[k][9],ordenando[k][10],ordenando[k][11],ordenando[k][12],ordenando[k][13]);
            Sistema.push_back(C);
        }

    }
    //cerrando el archivo de entrada
    fentrada.close();

    //se abre o se crea el archivo datos.txt en modoescritura, donde saldran las soluciones calculadas
    std::ofstream outfile;
    outfile.open("datos.txt");
	//Ciclo para N-1 pasos de tiempo (imprime N valores para cada cuerpo)
	for (int i = 0; i < N; i++){

        for (int j = 0; j < Sistema.size(); j++){
            //da el siguiente paso y se imprime en datos.txt, el algoritmo se autoinicia
             Tstep(Sistema.at(j));
			 outfile<< Sistema.at(j).x.at(0) << "\t\t" << Sistema.at(j).x.at(1) << "\t\t" << Sistema.at(j).x.at(2)<<"\n";

        }
        //limpia todas las fuerzas sobre un cuerpo, para dar e siguiente paso
         for (int j = 0; j < Sistema.size(); j++){
             limpF(Sistema.at(j));
         }
		//Interacion entre todos los cuerpos del sistema
		 for (int j = 0; j < Sistema.size(); j++){
             for (int k = 0; k < Sistema.size()-1; k++){
                 if (j!=k){
                     	NewF(Sistema.at(j),Sistema.at(k));
                 }
			}
		}

		//actualiza velocidad y aceleracion
		 for (int j = 0; j < Sistema.size(); j++){
             Vstep(Sistema.at(j));
		 }
         //termina deescribir sobre datos.txt
		 outfile<<std::endl;
	}
    //cierra datos.txt
    outfile.close();
	return 0;
}
void limpF(cuerpo&a){  //funcion para hacer la fuerza total sobre un cuerpo igual a cero, al iniciar una nueva interacion

	a.F.at(0) =0 ;
	a.F.at(1) =0;
	a.F.at(2) =0;
}

void NewF(cuerpo &a, cuerpo &b){       //calcula la fuerza que ejerce el cuerpo b sobre el cuerpo a,

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

	// fuerza sobre lel cuerpo a

	double Fa = -G*b.m*a.m/r3;

	a.F.at(0) += Fa*R.at(0)*1;
	a.F.at(1) += Fa*R.at(1)*1;
	a.F.at(2) += Fa*R.at(2)*1;



}




void Vstep(cuerpo &a){   //algoritmo lp para la aceleracion y velocidad

    std::vector<double> An{0,0,0};
    An.at(0) = a.F.at(0)/a.m;
    An.at(1) = a.F.at(1)/a.m;
    An.at(2) = a.F.at(2)/a.m;

    a.v.at(0) += 0.5*(a.A.at(0)+An.at(0))*a.dt;
    a.v.at(1) += 0.5*(a.A.at(1)+An.at(1))*a.dt;
    a.v.at(2) += 0.5*(a.A.at(2)+An.at(2))*a.dt;

    a.A.at(0) = An.at(0) ;
    a.A.at(1) =  An.at(1);
    a.A.at(2) =  An.at(2);

}
void Tstep(cuerpo &a){         //algoritmo lp para el siguiente paso en la posicion

	a.x.at(0) += a.v.at(0)*a.dt+0.5*a.A.at(0)*pow(a.dt,2);
	a.x.at(1) += a.v.at(1)*a.dt+0.5*a.A.at(1)*pow(a.dt,2);
	a.x.at(2) += a.v.at(2)*a.dt+0.5*a.A.at(2)*pow(a.dt,2);

}
