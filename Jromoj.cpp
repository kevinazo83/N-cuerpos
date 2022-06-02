#include <iostream>
#include <vector>
#include<time.h>
#include <cmath>

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

	//Distancia entre dos cuerpos (Incompleto)
	double R(cuerpo a, cuerpo b);

	
int main(){

	srand(time(0));
	std::vector<cuerpo>Sistema;
	cuerpo c0;
	for (int i = 0; i < 3; i++){
		
		c0.init(rand()%9+1,rand()%9+1,rand()%9+1,rand()%9+1,rand()%9+1,rand()%9+1,rand()%9+1);
		Sistema.push_back(c0);
	}
	Sistema.at(0).print();
	Sistema.at(1).print();
	Sistema.at(2).print();
	
	std::cout<< R(Sistema.at(0),Sistema.at(1)) << "\n";
	return 0;
}

double R(cuerpo a, cuerpo b){
	
	double r = 0;
	for (int i=0; i <= 2; i++){
		r += pow((a.x.at(i)-b.x.at(i)),2);
	}
	r = sqrt(r);
	return r;
}
