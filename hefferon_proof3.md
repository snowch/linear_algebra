We've seen examples of all three happening so we need only prove
that there are no other possibilities.

First observe a homogeneous system with
at least one non- $\vec{0}$ solution $\vec{v}$ has infinitely many
solutions.

This is because any scalar multiple of~$`\vec{v}`$ also solves the homogeneous
system and there are infinitely many vectors in the set of scalar 
multiples of

$\vec{v}$: if $s,t\in\mathbb{R}$ are unequal then $s\vec{v}\neq t\vec{v}$,
since $s\vec{v}-t\vec{v}=(s-t)\vec{v}$ is
non- $\vec{0}$ as  any non- $\vec{0}$ component of $\vec{v}$, when 
rescaled by the non- $\vec{0}$ factor $s-t$, will give a non- $\vec{0}$ value.

Now apply Lemma 3.8 to conclude that a solution set

```math
\begin{equation*}
  \set{\vec{p}+\vec{h} |
    \text{\( \vec{h} \) solves the associated homogeneous system}}
\end{equation*}
```

is either empty (if there is no particular solution $` \vec{p} `$),
or has one element (if there is a $` \vec{p} `$ and the homogeneous system
has the unique solution $\vec{0}$), or is infinite (if there is a
$` \vec{p} `$ and the homogeneous system has a non- $\vec{0}$ solution,
and thus by the prior paragraph has infinitely many solutions).
