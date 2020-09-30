CXX = g++
CXXFLAGS = -Wall -Werror -Wextra -pedantic -std=c++17 -g -fsanitize=address
LDFLAGS =  -fsanitize=address

SRC = ./
OBJ = $(SRC:.cc=.o)
EXEC = main

# all: 

fila1: $(SRC)Fila1/fila.cpp $(SRC)Fila1/teste.cpp 
	$(CXX) -c .$(SRC)/Fila1/fila.cpp && $(CXX) -c $(SRC)/Fila1/teste.cpp && $(CXX) -o teste fila.o teste.o

fila2: $(SRC)Fila2/fila.cpp $(SRC)Fila2/teste.cpp 
	$(CXX) -c $(SRC)Fila2/fila.cpp && $(CXX) -c $(SRC)Fila2/teste.cpp && $(CXX) -o teste fila.o teste.o

grafo: $(SRC)Grafo/grafo.cpp
	$(CXX) -c $(SRC)Grafo/grafo.cpp 

bfs: grafo $(SRC)Grafo/grafo.cpp
	$(CXX) $(SRC)bfs.cpp -o bfs

# $(EXEC): $(OBJ)
# 	$(CXX) $(LDFLAGS) -o $@ $(OBJ) $(LBLIBS)

clean:
	rm -rf *.o teste