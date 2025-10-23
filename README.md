# Genetic Algorithm for Solving an Equation

## Description

This project implements a **genetic algorithm (GA)** to find the solution of a mathematical equation with three variables (x, y, z). Each solution is represented as a chromosome consisting of three genes. The algorithm iteratively evolves a population to minimize the **fitness function**, which represents the error of the equation. The goal is to find values of x, y, z that satisfy the equation exactly (fitness = 0).

---

## Equation (Fitness Function)

The fitness function used in this project is:

```
fitness = | 2*x^2 + 3*y^2 + z - 2*x*y + 10*x*z - 5 |
```

The closer the value is to zero, the better the solution.

---

## Genetic Algorithm Components

* **Gene:** Each variable (x, y, z) represents a gene.

* **Chromosome:** `[x, y, z]` — an array of three genes.

* **Individual (Solution):** Each solution is a single chromosome.

* **Initial Population:** 6 individuals with random values:

  * x, y ∈ [-20, 20]
  * z ∈ [-100, 100]

* **Selection:** Solutions are ranked by fitness. The top three solutions are selected and paired to create six offspring via **crossover**.

* **Crossover:** Two crossover points:

  * Child 1: x and z from parent 1, y from parent 2
  * Child 2: x and z from parent 2, y from parent 1

* **Mutation:** 25% of all genes (2 genes per 3 randomly selected chromosomes) are mutated:

  * x or y → random integer [-20, 20]
  * z → random integer [-100, 100]

* **Termination Condition:** Algorithm stops when a solution achieves **fitness = 0**, i.e., the equation is exactly satisfied.

---

## How to Run

1. Make sure you have **Python 3** installed.
2. Save the code as `genetic_algorithm.py`.
3. Run the script:

```bash
python genetic_algorithm.py
```

---

## Sample Output

```
initial population : [[10, -5, 32], [-8, 15, -10], ...]
x: 1, y: 2, z: 3
count: 59
```

> The solution is `[x, y, z]` with fitness = 0, reached after 59 generations (varies depending on initial population).

---

## Dependencies

* Python standard library: `random`, `math`

---

## Notes

* The number of generations required to reach a solution depends on the initial population.
* This implementation is a simple demonstration of GA concepts: selection, crossover, mutation, and fitness evaluation.
