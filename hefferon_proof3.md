**Proof** [Nonhomogeneous Systems](https://en.wikibooks.org/wiki/Linear_Algebra/General_%3D_Particular_%2B_Homogeneous) (General = Particular + Homogeneous)

We've seen examples of all three happening so we need only prove that those are the only possibilities.

First, notice a homogeneous system with at least one $`non-\vec{0}`$ solution $`\vec{v}`$ has infinitely many solutions because the set of multiples $`s\vec{v}`$ is infinite&mdash; if $`s\neq 1`$ then $`s\vec{v}-\vec{v}=(s-1)\vec{v}`$ is easily seen to be $`non-\vec{0}`$, and so $`s\vec{v}\neq \vec{v}`$.

Now, apply Lemma 3.8 to conclude that a solution set

```math
\{\vec{p}+\vec{h}\,\big|\,\vec{h} \text{ solves the associated homogeneous system}\}
```

is either empty (if there is no particular solution $` \vec{p} `$), or has one element (if there is a $` \vec{p} `$ and the homogeneous system has the unique solution $`\vec{0}`$), or is infinite (if there is a $` \vec{p} `$ and the homogeneous system has a $`non-\vec{0}`$ solution, and thus by the prior paragraph has infinitely many solutions).

---

In the provided text, there's an explanation of why a homogeneous system with at least one non-zero solution has infinitely many solutions. This is because if we have a non-zero solution vector $` \vec{v} `$, then any multiple of this vector $` s\vec{v} `$ will also be a solution. If we choose $` s \neq 1 `$, then the vector $` s\vec{v} - \vec{v} `$ will also be a solution, which guarantees that there are infinitely many solutions.

Now, let's apply this explanation to the given example:

$`
\begin{align*}
x + y + z &= 0 \\
0x + y - z &= 0 \\
x + 2y + 0z &= 0
\end{align*}
`$

The solution set for this system is $` x = -2z `$ and $` y = z `$.

In this example, $` \vec{v} `$ is the non-zero solution vector. It represents the solution $` (x, y, z) = (-2z, z, z) `$. Here, $` \vec{v} = \begin{pmatrix} -2 \\ 1 \\ 1 \end{pmatrix} `$.

Now, let's consider multiples of $` \vec{v} `$, denoted as $` s\vec{v} `$. Any multiple of $` \vec{v} `$ will be a solution to the system. For instance, if we take $` s = 2 `$, then $` s\vec{v} = 2 \cdot \vec{v} = 2 \cdot \begin{pmatrix} -2 \\ 1 \\ 1 \end{pmatrix} = \begin{pmatrix} -4 \\ 2 \\ 2 \end{pmatrix} `$, which is also a solution to the system.

This means that the solution set is not just one solution, but rather a whole line of solutions, with each point on the line being a multiple of $` \vec{v} `$. Therefore, the system has infinitely many solutions, as explained in the text.
