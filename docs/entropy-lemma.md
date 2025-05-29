# Entropy Lemma

## Preliminaries
- Hilbert space $\mathcal{H}=\mathbb{C}^2$
- Entropy metric: $H(p)=-\sum p_i \ln p_i$
- Collapse: for $\psi=(a,b)$, $p_i=|\psi_i|^2/\sum_j|\psi_j|^2$

## Lemma 1 (Necessity)
If $H(p)<\ln 2$ then the configuration is inactive.
*Proof.* $H(p)$ maximal $\ln 2$ when $p=(\tfrac12,\tfrac12)$. Smaller $H$ means imbalance $→$ no symmetry.

## Lemma 2 (Sufficiency)
If $H(p)=\ln 2$ then the configuration is active.
*Proof.* $p=(\tfrac12,\tfrac12)$ yields maximal entropy, matching symmetry condition.

## Example
State $\psi=\tfrac{1}{\sqrt2}(1,1)$ $→$ $p=(\tfrac12,\tfrac12)$, so $H=\ln2$.

## Discussion
تقارن اطلاعاتی $H=\ln2$ مدل دو حالت «فعال/غیرفعال» است؛ هر انحرافی انرژی نگاه را می‌شکند.

```python
from sstai.core.entropy import entropy, collapse
import random, cmath
psi=[complex(random.random(),0) for _ in range(2)]
H=entropy(collapse(psi))
active=abs(H - math.log(2)) < 1e-6
print(H, active)
```
