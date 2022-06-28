all :: graficandoando.py

graficandoando.py :: datos.txt
	python3 graficandoando.py
datos.txt :: lp.exe
	./lp.exe
lp.exe :: VerletVelocidad.cpp entrada.txt
	g++ VerletVelocidad.cpp -o lp.exe
entrada.txt :: entrada.py
	python3 entrada.py
