#include <iostream>
#include <fstream>
#include <vector>

int main(){
	std::ifstream file_to_open("tc1.bin", std::ios::binary);
	std::ofstream file_to_write("tc1.txt");
	std::string text;
	if(file_to_open.is_open()){
		while(!file_to_open.eof()){
			file_to_open.read((char*)&text, sizeof(std::string));
			file_to_write << text;
		}
	}
	return 0;
}