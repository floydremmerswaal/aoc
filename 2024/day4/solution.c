#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>
#include <unistd.h>

#define INPUT "C:\\Users\\floyd\\aoc\\2024\\day4\\input.txt"
#define SIZE 140


int is_valid(char** arr, int i, int j) {
    if (i < 0 || i >= SIZE || j < 0 || j >= SIZE) {
        return 0;
    }
    return 1;
}

int check_pos(char** arr, int i, int j){
    char word[] = {'M', 'A', 'S'};
    int dx[] = {0, 0, 1, -1, 1, -1, 1, -1};
    int dy[] = {1, -1, 0, 0, 1, -1, -1, 1};

    int total = 0;

    for (int k = 0; k < 8; k++) {
        int x = i + dx[k];
        int y = j + dy[k];
        int cnt = 0;
        while (is_valid(arr, x, y) && arr[x][y] == word[cnt]) {
            cnt++;
            x += dx[k];
            y += dy[k];
        }
        if (cnt == 3) {
            total++;
        }
    }

    return total;

}

int check_pos_2(char** arr, int i, int j){
    if (i + 1 >= SIZE || i - 1 < 0 || j + 1 >= SIZE || j - 1 < 0) {
        return 0;
    }

    int total = 0;

    char ul = arr[i - 1][j - 1];
    char ur = arr[i - 1][j + 1];
    char dl = arr[i + 1][j - 1];
    char dr = arr[i + 1][j + 1];

    if ((ul == 'S'&& dr == 'M' || ul == 'M' && dr == 'S') && (ur == 'S' && dl == 'M' || ur == 'M' && dl == 'S')) {
        total++;
    }

    return total;
}


int main() {
    FILE* file;
    char ch;

    file = fopen(INPUT, "r");
    if (file == NULL) {
        printf("Error! Could not open file\n");
        exit(1);
    }

    // allocate memory for the array of strings
    char** arr = (char**)malloc(SIZE * sizeof(char*));
    for (int i = 0; i < SIZE; i++) {
        arr[i] = (char*)malloc(SIZE * sizeof(char));
    } 

    // read the file
    int i = 0;
    int j = 0;
    while ((ch = fgetc(file)) != EOF) {
        if (ch == '\n') {
            arr[i][j] = '\0'; // null-terminate the string
            i++;
            j = 0;
        } else {
            arr[i][j] = ch;
            j++;
        }
    }

    int cnt = 0;
    int cnt2 = 0;
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            if (arr[i][j] == 'X'){
                cnt += check_pos(arr, i, j);
            } else if (arr[i][j] == 'A') {
                cnt2 += check_pos_2(arr, i, j);
            }
        }
    }

    printf("Number of XMAS: %d\n", cnt);
    printf("Number of X-MAS: %d\n", cnt2);

    fclose(file);

    return 0;
}