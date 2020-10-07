CXX = g++
CXXFLAGS = -Wall -Werror -Wextra -pedantic -std=c++17 -g -fsanitize=address
LDFLAGS =  -fsanitize=address

SRC = ./
OBJ = $(SRC:.cc=.o)
EXEC = main

# all: 

grafo: $(SRC)Grafo/grafo.cpp
	$(CXX) -c $(SRC)Grafo/grafo.cpp 

dfs: grafo $(SRC)Grafo/grafo.cpp
	$(CXX) $(SRC)dfs.cpp -o dfs

# $(EXEC): $(OBJ)
# 	$(CXX) $(LDFLAGS) -o $@ $(OBJ) $(LBLIBS)

clean:
	rm -rf *.o dfs