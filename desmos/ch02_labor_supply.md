# Desmos guide: Chapter 2, Labor Supply

Open <https://www.desmos.com/calculator>. Use one graph for the labor-leisure diagram (Part A to D) and a second, separate graph for the labor supply curve (Part E). Type each line into its own expression row exactly as written (Desmos turns `alpha`, `<=` etc. into symbols automatically). Lines that define a value with `=` (for example `a=0.6`) become sliders: click "all" to set the range.

Axes for the diagram: `x` is **leisure** L (hours), `y` is **consumption** C ($). Set the viewport to x from 0 to 120 and y from 0 to 1500 (wrench icon, or Graph Settings).

The values in the notebook `notebooks/ch02_labor_supply.ipynb` are the baseline here, so you can compare numbers.

## How to enter the expressions

* Type each line into its own expression row. Names such as `epsilon_S`, `alpha`, `beta`, `delta`, `kappa`, `tau`, `rho` turn into Greek symbols when typed; `_` starts a subscript, press the right arrow to leave it. Where a subscripted name is followed by a bracket or another variable, a `*` is written explicitly so that Desmos reads a product.
* `^(` starts an exponent and `)` ends it; `/` makes a fraction, and the parentheses written around numerators and denominators keep the expression unambiguous.
* `{...}` after an expression is a restriction (type the brace; Desmos closes it). In a piecewise definition write `{condition: value, condition: value, default}`.
* `int[A to B] f(t) dt` means: type `int`, put `A` in the lower box and `B` in the upper box (use Tab), then type `f(t)dt`.
* A line like `a=0.6` becomes a slider; the text after the value in these listings (`slider ..., step ...`) is a comment for you, not part of the input. Do not type it.
* If a name is reused with a different meaning in a later part (for example `S`, `delta` or `V_m`), put that part in a new graph.

## A. Parameters (sliders)

```
a=0.6        slider 0.05 to 0.95, step 0.01   (weight on leisure in U = L^a C^(1-a))
w=10         slider 1 to 60, step 0.5         (wage)
V=100        slider 0 to 500, step 10         (non-labor income)
T=110        slider 80 to 112, step 1         (non-sleeping hours)
```

## B. Budget line and endowment point

```
y=w(T-x)+V{0<=x<=T}
```
Type the brace `{` and Desmos closes it; the condition restricts the line to 0≤x≤T. The slope is `-w`; it passes through the endowment point E = (T, V).

```
E_0=(T,V)
```
Label it (click the dot, then the label icon). Dragging `V` shifts the line in parallel (Figure 2-7); dragging `w` rotates it around E (Figure 2-8).

## C. Optimum and indifference curves

Closed-form optimum (the Cobb-Douglas solution from the notebook):

```
L_s=a(wT+V)/w
C_s=(1-a)(wT+V)
h_s=T-L_s
P=(L_s,C_s)
u_s=L_s^aC_s^(1-a)
```
Indifference curve through the optimum (implicit curve, type it exactly):

```
x^ay^(1-a)=u_s
```
Contours (a family of indifference curves, one per utility level). Type a separate line for each level, or use a list:

```
x^ay^(1-a)=[0.6,0.8,1.2,1.5]u_s
```
Desmos draws one curve per list entry. If your version does not accept lists in implicit equations, type four separate lines (`x^ay^(1-a)=0.6u_s`, and so on).

Fully manual check of the tangency: add a slider

```
u=100        slider 50 to 300, step 1
x^ay^(1-a)=u
```
and drag `u` upward until the curve just touches the budget line. It should touch at `P`, when `u` equals `u_s`.

**Baseline readings** (a=0.6, w=10, V=100, T=110): `L_s=72`, `C_s=480`, `h_s=38`, `u_s≈153.78`.

Tangency check: `MRS = a/(1-a) * C_s/L_s` should equal `w`:

```
((a)/(1-a))((C_s)/(L_s))
```
It evaluates to `10`.

## D. Income and substitution effects (Figure 2-9)

Add a second wage and the compensated point.

```
w_1=20       slider 1 to 60, step 0.5
y=w_1*(T-x)+V{0<=x<=T}
L_R=a(w_1*T+V)/w_1
C_R=(1-a)(w_1*T+V)
R=(L_R,C_R)
L_Q=u_s*(a/((1-a)w_1))^(1-a)
C_Q=(u_s/L_Q^a)^(1/(1-a))
Q=(L_Q,C_Q)
y=C_Q-w_1*(x-L_Q)
```
The last line is the compensated budget line: slope `-w_1`, tangent to the old indifference curve at Q.

Reading the picture: P to Q is the **substitution effect** (change in leisure `L_Q-L_s`, negative); Q to R is the **income effect** (`L_R-L_Q`, positive). Hours worked at each point: `T-L_s`, `T-L_Q`, `T-L_R`.

**Baseline readings** (w_1=20): `Q=(54.57, 727.54)`, `R=(69, 920)`. Hours: P 38, Q 55.4, R 41; substitution effect +17.4 hours, income effect -14.4 hours, total +3.

## E. Labor supply curve (second graph)

Open a new graph. Axes: `x` is **hours** h, `y` is the **wage**. Copy the sliders `a`, `V`, `T` from Part A (without `w`).

Cobb-Douglas labor supply written as w as a function of h (invert `h=(1-a)T-aV/w`):

```
y=((aV)/((1-a)T-x)){0<=x<(1-a)T}
```
Reservation wage (intercept at h=0):

```
w_R=((aV)/((1-a)T))
(0,w_R)
```
Baseline value: `w_R≈1.36`. Setting `V=0` makes the curve vertical at `x=(1-a)T`: income and substitution effects cancel exactly.

**CES version with a backward bend.** Add a slider `s=0.5` (elasticity of substitution, slider 0.2 to 4, step 0.1) and plot hours as a function of the wage using `x` as the dependent variable:

```
H(w)=max(0,T-(((wT+V)(a/w)^s)/(a^sw^(1-s)+(1-a)^s)))
x=H(y){y>0}
```
For `s<1` the curve bends back at high wages (try y up to 150 with `s=0.5`); for `s>1` it keeps rising.
Reading at `s=0.5`, `y=80`: `H(80)≈8.06` hours.

**Fixed cost and participation (optional).** Add a slider `F=40` and, because Desmos cannot compare two optima on its own, plot the two utilities against the wage:

```
U_w(w)=(T-h_F(w))^a(wh_F*(w)+V-F)^(1-a)
h_F(w)=max(0,(1-a)T-a(V-F)/w)
U_n=T^aV^(1-a)
```
Put `w` on x and plot `y=U_w(x)` and `y=U_n`; the crossing is the reservation wage with fixed cost (about 3.36 for F=40).

## F. Kinked budget sets (welfare and EITC)

Keep the diagram from Parts A to C. Add the program parameters:

```
G=250        slider 0 to 600, step 10   (welfare guarantee)
t=1          slider 0 to 1, step 0.05   (benefit reduction rate)
```
Welfare budget (earnings are `w(T-x)`; `abs` replaces `max` so the same formula works on lists later):

```
B_w(x)=w(T-x)+V+(((G-tw(T-x))+abs(G-tw(T-x)))/(2))
y=B_w(x){0<=x<=T}
```
With `t=1` the line is flat for the first `G/w` hours of work (every earned dollar is taken back), then rises with slope `-w`.

EITC budget:

```
s_e=0.4      Y_1=150      Y_2=250      p_p=0.2
c_r(x)={w(T-x)<=Y_1:s_e*w(T-x), w(T-x)<=Y_2:s_e*Y_1, max(0,s_e*Y_1-p_p*(w(T-x)-Y_2))}
B_e(x)=w(T-x)+V+c_r(x)
y=B_e(x){0<=x<=T}
```

**Finding the chosen point without a solver.** Make a list of leisure values, evaluate utility along the budget, and select the maximizer:

```
X=[0.5,1...110]
U_l=X^a B_e(X)^(1-a)
P_e=(X[U_l=max(U_l)],B_e(X[U_l=max(U_l)]))
```
Replace `B_e` by `B_w` for the welfare program. This is the same grid search as in the notebook. Baseline result for the EITC: leisure about 81.8 (hours about 28.2), `C≈436`.

If Desmos complains about `B_e(X)` on a list, define `B_e` as a function of `x` that uses only arithmetic and `abs` (no piecewise) or evaluate the piecewise version on single points instead.
