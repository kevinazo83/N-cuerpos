all :: a.out entrada.txt

entrada.txt :: N_planetas.txt
	python3 Entrada.py

a.out :: entrada.txt
	g++ Verlet.cpp
	./a.out
