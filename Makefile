CXX = g++
CXXFLAGS = -std=c++17 -O2

TARGET = log_analyzer
SRC = main.cpp parser.cpp analyzer.cpp

all:
	$(CXX) $(CXXFLAGS) $(SRC) -o $(TARGET)

clean:
	rm -f $(TARGET)


