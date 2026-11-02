# Desmos guide: Chapter 4, Labor Market Equilibrium

Open <https://www.desmos.com/calculator>. Axes: `x` is **employment** E, `y` is the **wage** w. Viewport: x from 0 to 150, y from 5 to 40. Lines such as `E_0=100` that define a number create sliders; click "all" to set ranges. Each part below can go in the same graph or in a fresh one.

Values match `notebooks/ch04_labor_market_equilibrium.ipynb`.

## How to enter the expressions

* Type each line into its own expression row. Names such as `epsilon_S`, `alpha`, `beta`, `delta`, `kappa`, `tau`, `rho` turn into Greek symbols when typed; `_` starts a subscript, press the right arrow to leave it. Where a subscripted name is followed by a bracket or another variable, a `*` is written explicitly so that Desmos reads a product.
* `^(` starts an exponent and `)` ends it; `/` makes a fraction, and the parentheses written around numerators and denominators keep the expression unambiguous.
* `{...}` after an expression is a restriction (type the brace; Desmos closes it). In a piecewise definition write `{condition: value, condition: value, default}`.
* `int[A to B] f(t) dt` means: type `int`, put `A` in the lower box and `B` in the upper box (use Tab), then type `f(t)dt`.
* A line like `a=0.6` becomes a slider; the text after the value in these listings (`slider ..., step ...`) is a comment for you, not part of the input. Do not type it.
* If a name is reused with a different meaning in a later part (for example `S`, `delta` or `V_m`), put that part in a new graph.

## A. One competitive market (4-1)

```
w_0=20        E_0=100
epsilon_S=0.5     slider 0.05 to 5, step 0.05   (supply elasticity)
delta=-0.75   slider -5 to -0.1, step 0.05  (demand elasticity)
g_s=1         slider 0.5 to 1.5, step 0.01  (supply shift factor)
g_d=1         slider 0.5 to 1.5, step 0.01  (demand shift factor)
```
Curves with `x` as the dependent variable:

```
x=g_s*E_0(y/w_0)^(epsilon_S)
x=g_d*E_0(y/w_0)^(delta)
```
Equilibrium (closed form; Desmos cannot solve equations by itself):

```
w_e=w_0*(g_d/g_s)^(1/(epsilon_S-delta))
E_e=g_s*E_0(w_e/w_0)^(epsilon_S)
(E_e,w_e)
```
Check: `g_d=1.1`, `g_s=1` gives `(103.89, 21.585)`; `g_s=1.1`, `g_d=1` gives `(105.89, 18.53)`. Drag `epsilon_S` and `delta` to see how the response of wages and employment to a shift depends on the elasticities.

## B. Two markets and migration (4-2)

Two regions, same `delta`; region B has lower productivity.

```
kappa_A=1      kappa_B=0.6      N=200
V_A(E)=kappa_A*w_0(E/E_0)^(1/delta)
V_B(E)=kappa_B*w_0((N-E)/E_0)^(1/delta)
y=V_A(x){0<x<N}
y=V_B(x){0<x<N}
```
`x` is employment in region A and `N-x` is employment in B. Start with `N_A=100` (no migration):

```
N_A=100
(N_A,V_A(N_A))
(N_A,V_B(N_A))
```
Equilibrium with free mobility (closed form: `kappa_A x^(1/delta)=kappa_B (N-x)^(1/delta)`):

```
E_A=((N)/(1+(kappa_A/kappa_B)^(delta)))
(E_A,V_A(E_A))
```
Check: `E_A=118.9`, common wage `15.87`, wages before migration 20.00 and 12.00. Gain in output is the area between the two curves from `N_A` to `E_A`:

```
G=int[N_A to E_A]V_A(t)dt-int[N-E_A to N-N_A]V_C(t)dt
```
where `V_C(t)=kappa_B*w_0(t/E_0)^(1/delta)` is the region B curve written in terms of its own employment. Expected value: about `76.1`.

## C. Payroll tax and deadweight loss (4-3)

Desmos has no equation solver, so choose the tax wedge by choosing the new employment `E_t` and read the implied tax (`tau`) from the gap between the curves:

```
E_t=97       slider 50 to 100, step 0.1
S_i(E)=w_0*(E/E_0)^(1/epsilon_S)
D_i(E)=w_0*(E/E_0)^(1/delta)
tau=D_i(E_t)-S_i(E_t)
w_w=S_i(E_t)
w_f=D_i(E_t)
```
Plot the supply and demand curves from Part A (set `g_s=g_d=1`) and:

```
(E_t,w_w)
(E_t,w_f)
x=E_t{w_w<=y<=w_f}
```
Deadweight loss (shaded area between the curves) and its triangle approximation:

```
W_L=int[E_t to E_0](D_i(t)-S_i(t))dt
((1)/(2))*tau*(E_0-E_t)
```
To shade it, type `S_i(x)<=y<=D_i(x){E_t<=x<=E_0}`.

Worker share of the burden for a small tax:

```
((|delta|)/(epsilon_S+|delta|))
```
Check: `E_t=97.02` corresponds to `tau=2`, with `w_w=18.82`, `w_f=20.82`, worker share 0.588 (0.6 in the limit), `W_L≈2.98`. Drag `epsilon_S` to 0.05 and then 5 to see the burden fall almost entirely on workers, then almost entirely on firms.

## D. Mandated benefit (4-4)

Add a benefit cost `b` and the workers' valuation share `v`. Again pick the employment level and read the implied wedge: workers supply `E` hours at cash wage `S_i(E)-v b`; the employer pays `D_i(E)-b` at that employment; they agree at the equilibrium employment.

```
b=3        slider 0 to 8, step 0.25
v=0.5      slider 0 to 1, step 0.05
x=E_0*((y+vb)/w_0)^(epsilon_S)
x=E_0*((y+b)/w_0)^(delta)
```
The two curves intersect at the new equilibrium (click the intersection point to read it). For `v=1` the intersection is at `x=100` and `y=17`: wage falls by exactly `b` and employment is unchanged. For `v=0` the intersection matches the payroll-tax equilibrium for `tau=b` (`E=95.54`, `w=18.255`). At `v=0.5`: `E=97.76`, `w=17.61`.

## E. Immigration and the immigration surplus (4-5, 4-6)

Inelastic native supply `N=E_0` (vertical line) plus `M` immigrants:

```
m=0.10      slider 0 to 0.4, step 0.01
M=mE_0
w_1=w_0*((E_0+M)/E_0)^(1/delta)
x=E_0
x=E_0+M
y=w_0*(x/E_0)^(1/delta)
```
Surplus (extra output minus the immigrants' earnings), and the triangle approximation:

```
W_s=int[E_0 to E_0+M]w_0*(t/E_0)^(1/delta)dt-w_1*M
((1)/(2))*(w_0-w_1)*M
```
Check (`delta=-0.75`, `m=0.1`): `w_1=17.61`, `W_s=11.49`, approximation `11.93`. Set `delta=-2.5` for a narrow skill group: `w_1=19.25`, surplus `3.66`. Shade the surplus with `w_1<=y<=w_0*(x/E_0)^(1/delta){E_0<=x<=E_0+M}`.

For *elastic* native supply the supply curve shifts right by `M`:

```
x=E_0*(y/w_0)^(epsilon_S)+M
x=E_0*(y/w_0)^(delta)
```
Click the intersection: at `epsilon_S=0.5`, `delta=-0.75`, `m=0.1` it is at `w=18.48`.

## F. Monopsony (4-9)

```
epsilon_m=2        slider 0.5 to 10, step 0.1   (firm-level supply elasticity)
delta=-0.75
V_m(x)=w_0*(x/E_0)^(1/delta)
S(x)=w_0*(x/E_0)^(1/epsilon_m)
M_c(x)=S(x)(1+1/epsilon_m)
y=V_m(x)
y=S(x)
y=M_c(x)
```
Monopsony point (closed form):

```
E_m=E_0*(1+1/epsilon_m)^(1/(1/delta-1/epsilon_m))
w_m=S(E_m)
(E_m,V_m(E_m))
(E_m,M_c(E_m))
(E_m,w_m)
((w_m)/(V_m(E_m)))
```
Check: `E_m=80.16`, `w_m=17.91`, `V_m(E_m)=26.86`, and the last expression equals `epsilon_m/(1+epsilon_m)=0.667`.

Deadweight loss: `int[E_m to E_0](V_m(t)-S(t))dt` (about `82.6`).

Minimum wage under monopsony: add a slider and the employment rule (for a binding minimum wage `w_b`)

```
w_b=19      slider 10 to 30, step 0.25
y=w_b
x=E_0*(w_b/w_0)^(epsilon_m){w_b>w_m}
```
For `w_m<w_b<=w_0` employment is `S`'s value `E_0*(w_b/w_0)^(epsilon_m)`, which is greater than `E_m`. At `w_b=20` (the competitive wage) employment is 100. Above `w_0`, employment is the demand value `E_0*(w_b/w_0)^(delta)`, which falls. Drag `w_b` and watch the maximum at `w_0`.
