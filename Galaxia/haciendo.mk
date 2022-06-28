all :: dgalaxia.py

dgalaxia.py :: datos.txt
	python3 dgalaxia.py
datos.txt :: lp1.exe
	./lp1.exe
lp1.exe :: VerletVelocidad.cpp entrada.txt
	g++ VerletVelocidad.cpp -o lp1.exe
entrada.txt :: galaxia.py
	python3 galaxia.py
