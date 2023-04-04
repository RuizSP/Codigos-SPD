#include <iostream>
#include <vector>
#include <chrono>

using namespace std;

#define MAX_VALUE 100 + 1
#define MIN_VALUE -100
#define DELIMITER '|'

int row_matriz_a, col_matriz_a, row_matriz_b, col_matriz_b;
int **matriz_a, **matriz_b, **matriz_c;

vector<string> split_input(string str)
{
  vector<string> tokens;
  string token;

  for (const auto &c : str)
  {
    if (c == DELIMITER)
    {
      tokens.push_back(token);
      token.clear();
    }
    else
    {
      token += c;
    }
  }
  tokens.push_back(token);
  return tokens;
}

int **create_matriz(int row, int col)
{
  // criar matirz de forma dinamica
  int **matriz = new int *[row];
  for (int i = 0; i < row; i++)
  {
    matriz[i] = new int[col];
  }
  return matriz;
}

int **generate_random_matriz(int row, int col)
{
  int **matriz = create_matriz(row, col);

  // acessar e atribuir valores aleatorios na matriz
  for (int i = 0; i < row; i++)
  {

    for (int j = 0; j < col; j++)
    {

      matriz[i][j] = rand() % (MAX_VALUE - MIN_VALUE) + MIN_VALUE;
    }
  }

  // retornar a matriz pronta
  return matriz;
}

void multiply_row(int row)
{
  for (int i = 0; i < col_matriz_b; i++)
  {
    for (int j = 0; j < row_matriz_b; j++)
    {
      matriz_c[row][i] += matriz_a[row][j] * matriz_b[j][i];
    }
  }
}

void multiply_matriz()
{

  for (int i = 0; i < row_matriz_a; i++)
  {
    for (int j = 0; j < col_matriz_b; j++)
    {
      for (int k = 0; k < row_matriz_b; k++)
      {
        matriz_c[i][j] += matriz_a[i][k] * matriz_b[k][j];
      }
    }
  }
}

void print_matriz(int **matriz, int row, int col)
{
  for (int i = 0; i < row; i++)
  {
    for (int j = 0; j < col; j++)
    {
      cout << matriz[i][j] << "\t";
    }
    cout << endl;
  }
}

int main()
{

  // Leitura do input e tratamento da informação
  string input, str;
  cin >> str;
  vector<string> inputs = split_input(str);
  row_matriz_a = stoi(inputs[0]);
  col_matriz_a = stoi(inputs[1]);
  row_matriz_b = stoi(inputs[2]);
  col_matriz_b = stoi(inputs[3]);

  // criação da matriz com valores aleatorios
  matriz_a = generate_random_matriz(row_matriz_a, col_matriz_a);
  matriz_b = generate_random_matriz(row_matriz_b, col_matriz_b);
  matriz_c = create_matriz(row_matriz_a, col_matriz_b);
  
    auto start = std::chrono::high_resolution_clock::now();
  multiply_matriz();
  auto end = std::chrono::high_resolution_clock::now();
	
  auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start).count();
  
  float tempo = (float(duration)/1000000.0);
  
  cout << tempo << endl;

  return 0;
}
