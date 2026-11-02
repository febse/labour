# Desmos guide: Chapter 3, Labor Demand

Open <https://www.desmos.com/calculator>. Use one graph for the input space (isoquants and isocosts, Parts A to C) and a second graph for the demand curves (Part D). A line such as `a=0.3` creates a slider; click "all" to set its range.

Input-space axes: `x` is **labor** E, `y` is **capital** K. Viewport: x from 0 to 80, y from 0 to 90.

Values match `notebooks/ch03_labor_demand.ipynb`.

## How to enter the expressions

* Type each line into its own expression row. Names such as `epsilon_S`, `alpha`, `beta`, `delta`, `kappa`, `tau`, `rho` turn into Greek symbols when typed; `_` starts a subscript, press the right arrow to leave it. Where a subscripted name is followed by a bracket or another variable, a `*` is written explicitly so that Desmos reads a product.
* `^(` starts an exponent and `)` ends it; `/` makes a fraction, and the parentheses written around numerators and denominators keep the expression unambiguous.
* `{...}` after an expression is a restriction (type the brace; Desmos closes it). In a piecewise definition write `{condition: value, condition: value, default}`.
* `int[A to B] f(t) dt` means: type `int`, put `A` in the lower box and `B` in the upper box (use Tab), then type `f(t)dt`.
* A line like `a=0.6` becomes a slider; the text after the value in these listings (`slider ..., step ...`) is a comment for you, not part of the input. Do not type it.
* If a name is reused with a different meaning in a later part (for example `S`, `delta` or `V_m`), put that part in a new graph.

## A. Parameters

```
A=50         slider 10 to 100, step 1       (productivity)
alpha=0.3    slider 0.05 to 0.6, step 0.01  (capital exponent)
beta=0.5     slider 0.2 to 0.7, step 0.01   (labor exponent; keep alpha+beta<1)
p=1          slider 0.5 to 2, step 0.05     (output price)
w=10         slider 2 to 30, step 0.5       (wage)
r=10         slider 2 to 30, step 0.5       (rental price of capital)
```

## B. Isoquants and isocost (cost minimization)

Isoquant for output `q` (implicit curve, `y` is K and `x` is E):

```
q=907.7      slider 100 to 2000, step 10
A y^(alpha) x^(beta)=q
```
A family of isoquants (the contour map):

```
A y^(alpha) x^(beta)=[0.4,0.7,1,1.4]q
```
Cost-minimizing point for the chosen `q` (tangency):

```
k=((alpha w)/(beta r))
E_c=(q/A)^(1/(alpha+beta))(1/k)^(alpha/(alpha+beta))
K_c=kE_c
(E_c,K_c)
C_c=wE_c+rK_c
wx+ry=C_c
```
The last line is the isocost through the optimum; it is tangent to the isoquant at `(E_c,K_c)`. Drag `q` to move to a higher or lower isoquant and watch the tangency point trace the expansion path (a straight line of slope `k` through the origin, `y=kx`; add it to see this).

Drag `w`: the isocost rotates and the tangency point moves to a more capital-intensive mix (substitution effect).

Check at `q=907.7`, `w=r=10`: `(E_c,K_c)=(45.39, 27.23)`.

## C. Profit maximization and the decomposition into substitution and scale effects

Unconditional (long-run) factor demands from the first-order conditions `w=p MP_E`, `r=p MP_K`:

```
E_s=(((w)/(p*A*beta k^(alpha))))^(1/(alpha+beta-1))
K_s=kE_s
q_s=AK_s^(alpha)E_s^(beta)
(E_s,K_s)
```

Baseline reading: `E_s=45.39`, `K_s=27.23`, `q_s=907.7`, profit `p q_s - wE_s - rK_s=181.55`.

To reproduce Figure 3-14, store the old optimum and then raise the wage:

```
w_0=10        (fixed, old wage)
E_A=45.39     K_A=27.23     q_A=907.7     (type these as plain numbers)
w_1=15        slider 10 to 30, step 0.5
```
Point A: `(E_A,K_A)`.

Point B, the cost-minimizing mix at the new wage for the old output (substitution effect):

```
k_1=((alpha w_1)/(beta r))
E_B=(q_A/A)^(1/(alpha+beta))(1/k_1)^(alpha/(alpha+beta))
K_B=k_1*E_B
(E_B,K_B)
w_1*x+ry=w_1*E_B+rK_B
```
Point C, the new profit-maximizing choice (scale effect):

```
E_C=(((w_1)/(p*A*beta k_1^(alpha))))^(1/(alpha+beta-1))
K_C=k_1*E_C
(E_C,K_C)
A y^(alpha)x^(beta)=A K_C^(alpha)E_C^(beta)
w_1*x+ry=w_1*E_C+rK_C
```
Readings at `w_1=15`: `B=(38.98, 35.09)`, `C=(10.98, 9.88)` with `q_C≈329.4`. Substitution effect on labor: `E_B-E_A=-6.40`; scale effect: `E_C-E_B=-28.00`.

## D. Labor demand curves (second graph)

Axes: `x` is **labor** E, `y` is the **wage**. Viewport x from 0 to 100, y from 0 to 30. Copy the sliders `A`, `alpha`, `beta`, `p`, `r`.

Short run: capital fixed at `K_0`:

```
K_0=27.23    slider 5 to 80, step 0.5
y=p*A*beta K_0^(alpha)x^(beta-1)
```
This is the `V_m_E` curve, the short-run demand curve (hire up to where `V_m_E = w`). Add the wage line `y=w` (slider `w=10`) and the intersection: `E_s*r=(p*A*beta K_0^(alpha)/w)^(1/(1-beta))`.

Long run (capital adjusts), wage as a function of employment: invert the long-run demand function. Define

```
E_L(w)=(((w)/(p*A*beta(alpha w/(beta r))^(alpha))))^(1/(alpha+beta-1))
x=E_L(y){y>0}
```
The long-run curve is flatter than the short-run curve, crossing it at the wage for which `K_0` is the optimal capital stock (`w=10` here). Elasticities (add as expressions to read them):

```
epsilon_S*R=-((1)/(1-beta))
epsilon_L*R=-((1-alpha)/(1-alpha-beta))
```
Baseline values: `-2` and `-3.5`.

## E. Elasticity of substitution (isoquant shapes)

In the input-space graph (or a fresh one) add normalized CES isoquants through the point (50, 50):

```
a_c=0.4      slider 0.1 to 0.9, step 0.05
s=0.5        slider 0.1 to 5, step 0.1    (sigma, not equal to 1)
rho=1-1/s
a_c*(y/50)^rho+(1-a_c)(x/50)^rho=1
```
Type `rho` as `rho` (Desmos converts it). All values of `s` give isoquants through (50, 50) with the same slope there; low `s` makes them nearly L-shaped, high `s` nearly straight. For `s=1` Desmos cannot evaluate `rho=0`; use the Cobb-Douglas curve `y=50(x/50)^(-(1-a_c)/a_c)` instead.

## F. Minimum wage (competitive model)

In the demand graph add a supply curve and a minimum wage:

```
E_0=100   w_e=20   epsilon_S=0.5   delta=-0.75
w_m=22     slider 20 to 40, step 0.5
x=E_0*(y/w_e)^(epsilon_S)
x=E_0*(y/w_e)^(delta)
y=w_m
```
Employment at the minimum wage is the demand value `E_0*(w_m/w_e)^(delta)` (93.1 at `w_m=22`); the gap to the supply value `E_0*(w_m/w_e)^(epsilon_S)` (104.9) is unemployment (11.8).
