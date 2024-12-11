#include <iostream>
#include <fstream>
#include <vector>

bool inBounds(int x, int y, std::vector<std::vector<char>> data)
{
    return x >= 0 && x < data.size() && y >= 0 && y < data.size();
}

void printData(std::vector<std::vector<char>> data, int locx, int locy, int dir)
{
    for (int y = 0; y < data.size(); y++)
    {
        for (int x = 0; x < data[y].size(); x++)
        {
            if (x == locx && y == locy)
            {
                if (dir == 0)
                    std::cout << "^";
                else if (dir == 1)
                    std::cout << ">";
                else if (dir == 2)
                    std::cout << "v";
                else if (dir == 3)
                    std::cout << "<";
                continue;
            }
            std::cout << data[y][x];
        }
        std::cout << std::endl;
    }
}

int main()
{
    std::vector<std::vector<char>> data = {{}};
    std::vector<std::pair<int, int>> path = {};
    int locx = 0;
    int locy = 0;
    int dir = 0; // 0 = up, 1 = right, 2 = down, 3 = left
    std::ifstream file("C:\\Users\\floyd\\aoc\\2024\\day6\\example.txt");

    std::string line;

    while (std::getline(file, line))
    {
        std::vector<char> row = {};
        for (char c : line)
        {
            if (c == '^')
            {
                path.push_back(std::make_pair(row.size(), data.size()));
                locx = row.size();
                locy = data.size();

                row.push_back('.');
                continue;
            }
            row.push_back(c);
        }
        data.push_back(row);
    }

    // print the data
    while (true)
    {
        printData(data, locx, locy, dir);
        int nextx = locx;
        int nexty = locy;
        if (dir == 0)
        {
            locy--;
            nexty = locy - 1;
        }
        else if (dir == 1)
        {
            locx++;
            nextx = locx + 1;
        }
        else if (dir == 2)
        {
            locy++;
            nexty = locy + 1;
        }
        else if (dir == 3)
        {
            locx--;
            nextx = locx - 1;
        }

        if (!inBounds(locx, locy, data))
        {
            break;
        }

        // before we hit a wall (we see a # in front of us), we turn right
        if (inBounds(nextx, nexty, data) && (data[nextx][nexty] == '#'))
        {
            dir = (dir + 1) % 4;
        }

        path.push_back(std::make_pair(locx, locy));
    }

    std::cout << "Path: ";
    for (int i = 0; i < path.size(); i++)
    {
        std::cout << "(" << path[i].first << ", " << path[i].second << ")";
        if (i < path.size() - 1)
        {
            std::cout << " -> ";
        }
    }
    std::cout << std::endl;
    std::cout << "Length: " << path.size() << std::endl;

    return 0;
}