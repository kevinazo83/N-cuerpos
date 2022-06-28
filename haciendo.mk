all :: graficandoando.py


graficandoando.py :: datos.txt
	python3 graficandoando.py
datos.txt :: lp.exe
	./lp.exe
lp.exe :: lp.cpp entrada.txt
	g++ lp.cpp -o lp.exe
entrada.txt :: entrada.py
	python3 entrada.py
