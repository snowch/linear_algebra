**Lemma:** 

For any homogeneous linear system there exist vectors $`\beta_1, \ldots, \beta_k`$ such that the solution set of the system is $` \{c_1\beta_1 + \ldots + c_k\beta_k \, | \, c_1, \ldots, c_k \in \mathbb{R}\} `$ where $`𝑘`$ is the number of free variables in an echelon form version of the system.



Let's proceed with the proof by induction.

**Base Case (k = 0):**
If the system has no free variables, then it must be a unique solution. In this case, the solution set is simply a singleton set containing the unique solution vector. So, the claim holds trivially.

**Inductive Hypothesis:**
Assume that for any homogeneous linear system with $` k `$ free variables, there exist vectors $` \beta_1, \ldots, \beta_k `$ such that the solution set of the system is $` \{c_1\beta_1 + \ldots + c_k\beta_k \, | \, c_1, \ldots, c_k \in \mathbb{R}\} `$.

**Inductive Step:**
Consider a homogeneous linear system with $` k + 1 `$ free variables. Let's denote the system as $` A\mathbf{x} = \mathbf{0} `$, where $` A `$ is the coefficient matrix and $` \mathbf{x} `$ is the vector of variables. By the existence of echelon form, we can find $` k `$ linearly independent vectors $` \beta_1, \ldots, \beta_k `$ such that the solution set of the system is $` \{c_1\beta_1 + \ldots + c_k\beta_k \, | \, c_1, \ldots, c_k \in \mathbb{R}\} `$.

Now, let's find a particular solution $` \mathbf{p} `$ to the system $` A\mathbf{x} = \mathbf{0} `$. This can be done by setting all free variables to zero and solving for the remaining variables. Let $` \mathbf{p} `$ be this particular solution.

Let $` \mathbf{v} `$ be any vector in the solution set of the system. Then, $` \mathbf{v} = \mathbf{p} + c_{k+1}\mathbf{v}_{k+1} `$, where $` c_{k+1} `$ is any real number and $` \mathbf{v}_{k+1} `$ is the vector corresponding to the last free variable.

Now, consider the vector $` \mathbf{v} - \mathbf{p} = c_{k+1}\mathbf{v}_{k+1} `$. Since $` \mathbf{v}_{k+1} `$ is the vector corresponding to the last free variable, it's a basis vector for the null space of $` A `$. Thus, any linear combination of $` \mathbf{v}_{k+1} `$ is also in the null space of $` A `$.

Therefore, any vector $` \mathbf{v} `$ in the solution set of the system can be represented as a linear combination of $` \beta_1, \ldots, \beta_k `$, plus a multiple of $` \mathbf{v}_{k+1} `$. Hence, the claim holds for $` k + 1 `$.

By the principle of mathematical induction, the claim holds for all $` k `$.
