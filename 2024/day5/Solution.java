import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Solution {

  public static int getMiddle(int[] pages) {
    return pages[pages.length / 2];
  }

  public static int checkRulesP2(int[] pages, List<int[]> rules) {
    for (int i = 0; i < rules.size(); i++) {
      int[] rule = rules.get(i);
      int left = rule[0];
      int right = rule[1];
      int leftIndex = -1;
      int rightIndex = -1;
      for (int j = 0; j < pages.length; j++) {
        if (pages[j] == left) {
          leftIndex = j;
        }
        if (pages[j] == right) {
          rightIndex = j;
        }
      }
      if (leftIndex == -1 || rightIndex == -1) {
        continue;
      }
      if (leftIndex > rightIndex) {
        int temp = pages[leftIndex];
        pages[leftIndex] = pages[rightIndex];
        pages[rightIndex] = temp;
      }
    }

    if (checkRulesP1(pages, rules)) {
      return getMiddle(pages);
    } else {
      // keep swapping untill we get the right order lol
      return checkRulesP2(pages, rules);
    }
  }

  public static boolean checkRulesP1(int[] pages, List<int[]> rules) {
    for (int i = 0; i < rules.size(); i++) {
      int[] rule = rules.get(i);
      int left = rule[0];
      int right = rule[1];
      int leftIndex = -1;
      int rightIndex = -1;
      for (int j = 0; j < pages.length; j++) {
        if (pages[j] == left) {
          leftIndex = j;
        }
        if (pages[j] == right) {
          rightIndex = j;
        }
      }
      if (leftIndex == -1 || rightIndex == -1) {
        continue;
      }
      if (leftIndex > rightIndex) {
        return false;
      }
    }

    return true;
  }

  public static void main(String[] args) {
    try {
      File myObj = new File("C:\\Users\\floyd\\aoc\\2024\\day5\\input.txt");
      Scanner myReader = new Scanner(myObj);
      List<int[]> rules = new ArrayList<>();
      boolean buildingRules = true;
      int sum = 0;
      int sum2 = 0;
      while (myReader.hasNextLine()) {
        String data = myReader.nextLine();
        if (data.equals("")) {
          buildingRules = false;
          continue;
        }
        if (buildingRules) {
          String[] rule = data.split("\\|");

          int left = Integer.parseInt(rule[0]);
          int right = Integer.parseInt(rule[1]);
          rules.add(new int[] { left, right });

        } else {
          int[] pagesInt = List.of(data.split(",")).stream().mapToInt(Integer::parseInt).toArray();
          if (checkRulesP1(pagesInt, rules)) {
            sum += getMiddle(pagesInt);
          } else {
            sum2 += checkRulesP2(pagesInt, rules);
          }

        }
      }
      System.out.println("sum: " + sum);
      System.out.println("sum2: " + sum2);
      myReader.close();
    } catch (FileNotFoundException e) {
      System.out.println("An error occurred.");
      e.printStackTrace();
    }
  }
}