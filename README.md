# stochasticDiffEQs
studying stochastic differential equations with the eventual goal of reaching the development of flow and diffusion models.



1 --> blackScholes_eulerMaruyama.ipynb

the idea of this notebook is to implement the euler-maruyama + milstein method to solve the black-scholes equation for an european call option. eventually, flow and diffusion models will be developed with the special interest of trying to solve PDEs with these techniques. 

the idea is to implement the euler-maruyama algorithm as a numerical solver for the black-scholes equation. this equation was chosen because it has a straight-forward analytical solution, to which the e-m method can be compared to.

```math
X_{t + h} = X_t + u_t(X_t)dt + \sigma_t dW_{t - s} = X_t + u_t(X_t)\cdot h + \sigma_t \epsilon \sqrt{h}
```
where

```math
\epsilon \sim \mathcal{N}(0, Id)
```