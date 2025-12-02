#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <threads.h>
#include <time.h>
#include <unistd.h>

typedef struct {
  char direction;
  int amount;
} Action;

typedef struct {
  Action *actions;
  int count;
} TotalActions;

int proper_mod(int n, int mod) {
  int result = n % mod;

  if (result < 0) {
    result += mod;
  }

  return result;
}

TotalActions get_actions(const char *filename) {
  // Initialize variables
  FILE *input_file = fopen(filename, "r");
  assert(input_file != NULL);

  char *line = NULL;
  size_t size = 0;
  size_t n_read = 0;
  size_t capacity = 10;
  Action *actions = malloc(sizeof(Action) * capacity);

  // getline will reallocate memory for the &line variable if it is not big
  // enough to hold the line, making it safe(ish) from buffer overflows
  while (getline(&line, &n_read, input_file) != -1) {
    // Resize result array if we need more space
    size++;
    if (size > capacity) {
      capacity *= 2;
      // realloc() will copy over data if a new block is allocated
      actions = realloc(actions, sizeof(Action) * capacity);
    }

    char direction;
    int amount;

    sscanf(line, "%c%d", &direction, &amount);

    assert(direction == 'L' || direction == 'R');
    assert(amount >= 0);

    Action action = {direction, amount};
    actions[size - 1] = action;
  }

  free(line);
  fclose(input_file);

  TotalActions totalActions = {actions, size};

  return totalActions;
}

void calculate_result() {
  clock_t start = clock();
  TotalActions totalActions = get_actions("input.txt");

  int current = 50;
  int n_zeroes = 0;
  int n_zero_passes = 0;

  for (int i = 0; i < totalActions.count; i++) {
    int prev = current;
    Action action = totalActions.actions[i];

    if (action.direction == 'L') {
      current -= action.amount;
    } else if (action.direction == 'R') {
      current += action.amount;
    }

    if (current == 0) {
      n_zeroes++;
    }

    n_zero_passes += abs(current / 100);

    if (prev != 0 && current < 0) {
      n_zero_passes += 1;
    }

    current = proper_mod(current, 100);
  }

  clock_t end = clock();

  printf("Number of zeroes: %d\n", n_zeroes);
  printf("Number of zero passes: %d\n", n_zero_passes);
  printf("Total: %d\n", n_zero_passes + n_zeroes);
  printf("Elapsed time: %.3fms", (end - start) / (double)CLOCKS_PER_SEC * 1000);
}

int main() {
  calculate_result();

  return 0;
}
