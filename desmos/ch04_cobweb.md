# Desmos guide: Chapter 4-7, The Cobweb Model

Open <https://www.desmos.com/calculator>. Axes: `x` is **employment** E (new graduates), `y` is the **wage** w. Viewport: x from 0 to 200, y from 0 to 60. Lines such as `s=0.25` that define a number create sliders. Text after the value (`slider ...`) is a comment, not input. Values match `notebooks/ch04_cobweb_model.ipynb`.

Typing tips as in `ch04_equilibrium.md`: `_` starts a subscript (right arrow to leave it), `delta`, `epsilon` turn into Greek letters, `^(` starts an exponent.

## A. Linear curves through (E_0, w_0)

```
w_0=20        E_0=100
epsilon_S=0.5   slider 0.05 to 2, step 0.01   (supply elasticity)
delta=-0.75     slider -3 to -0.2, step 0.01  (demand elasticity)
s=0.25          slider 0 to 0.6, step 0.01    (demand shift)
b=w_0/(-delta*E_0)
d=epsilon_S*E_0/w_0
a=w_0+b*E_0
c=E_0-d*w_0
a_1=(1+s)*a
```
Curves (old demand, new demand, supply of graduates E = c + d w):

```
y=a-b*x
y=a_1-b*x
x=c+d*y
```
Stability indicator (this equals `epsilon_S/|delta|`; cycle explodes when it exceeds 1):

```
k=b*d
```

## B. The wage path in closed form

Difference equation `w_{t+1}=(a_1-b c)-b d w_t`, solved as `w_t = w* + (-bd)^t (w_start - w*)`:

```
n=12            slider 1 to 40, step 1
w_s=(a_1-b*c)/(1+k)
w_start=a_1-b*E_0
W(t)=w_s+(-k)^t*(w_start-w_s)
Q(t)=c+d*W(t-1)
T=[0...n]
```
`W(t)` is the wage in period t and `Q(t)` the graduates entering in period t (for `t>=1`; in period 0 the graduates are `E_0`). The long-run point:

```
(Q(1000),w_s)
```
(only a rough marker for `k<1`; or use `E_s=c+d*w_s` and `(E_s,w_s)`).

Check with defaults: `w_start=31.67`, `w_s=27`, `W(1)=23.89`, `W(2)=29.07`.

## C. The cobweb path (Borjas Fig. 4-17)

Starting vertical segment (wage jumps along the vertical short-run supply at E_0):

```
(E_0,(1-u)*w_0+u*w_start){0<=u<=1}
```
Define the graduates in each period (period 0 is `E_0`):

```
G(t)={t=0:E_0,c+d*W(t-1)}
```
Horizontal segments (students react to wage `W(t)`, moving along supply) and vertical segments (market clears on new demand):

```
((1-u)*G(T)+u*G(T+1),W(T)){0<=u<=1}
(G(T+1),(1-u)*W(T)+u*W(T+1)){0<=u<=1}
```
Markers on the demand curve:

```
(G(T),W(T))
```
Here `u` is not defined anywhere: Desmos treats it as the parameter of a curve because of the restriction.

## D. Time series (separate graph)

Use `x` as time t, `y` as the wage:

```
(T,W(T))
y=w_s
```
Viewport x from 0 to 40.

## E. What to try

* `epsilon_S=0.5`, `delta=-0.75` (`k=0.67`): spiral inwards.
* `epsilon_S=0.75` (`k=1`): permanent two-period cycle.
* `epsilon_S=0.9` (`k=1.2`): spiral outwards; raise `n` and zoom out.
* Make demand more elastic (`delta=-1.5`) or supply less elastic and the cobweb stabilises.
