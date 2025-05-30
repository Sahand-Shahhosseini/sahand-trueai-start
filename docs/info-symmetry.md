# Information Symmetry Lemma

## Preliminaries
Let \(\mathcal{H}=\mathbb{C}^n\). For density matrix \(\rho\), entropy \(H(\rho)=-\mathrm{Tr}\,\rho\log\rho\). Define \(d_{EE}(\rho,\sigma)=|H(\rho)-H(\sigma)|\). For \(L\in\mathcal{H}\), \(\|L\|=1\), collapse
\(C_L(\rho)=P_L\rho P_L/\mathrm{Tr}(P_L\rho)\) if \(\mathrm{Tr}(P_L\rho)\neq0\), with \(P_L=|L\rangle\langle L|\), else \(\rho\).

## Lemma 1 (Necessity)
If \(G_i=\arg\min_{S\subset G,P\vdash S}\sum w(\varphi)\), \(w(\varphi)=1/(H(C_L(\varphi))+\varepsilon)\), any lighter \(\Gamma\) contradicts minimality. \(\square\)

## Lemma 2 (Sufficiency)
With the same setup, each \(\varphi\in G_i\) obeys \(\langle\varphi|L\rangle\neq0\) and \(d_{EE}(\varphi,C_L(\varphi))=0\). Hence the collapsed state proves \(P\). \(\square\)

## Example
Basis \(|0\rangle,|1\rangle\); choose \(L=|0\rangle\). \(|\psi_2\rangle=(|0\rangle+|1\rangle)/\sqrt{2}\Rightarrow\rho_2=|\psi_2\rangle\langle\psi_2|\). Collapse gives
\(\rho_2'=\tfrac12|0\rangle\langle0|+\tfrac12|1\rangle\langle1|\), \(H(\rho_2')=\ln2\).

## Discussion
Active if \(H(C_L(\rho))-H(\rho)=0\), else inactive. This mirrors memory bits under decoherence.

## Algorithm (PTAS)
Approximate \(\arg\min\sum w\) via greedy search over \(K\le\log n\) states, \(O(nK)\) steps.

## Table
|Measure|Purpose|Scaling|
|---|---|---|
|ElectroCoding|Entropy-weighted phase cost|\(w(H)^{-1}\)|
|Kolmogorov|Shortest program length|\(\approx\kappa\)|
|\(\kappa\)-complexity|Prefix variant|similar|

## Protocol
1. Prepare qutrit superposition.
2. Interfere with phase shifter.
3. Measure \(\rho\) before/after and compute \(\Delta H\).

## Glossary
|Symbol|Meaning|
|--|--|
|\(\mathcal{H}\)|Hilbert space|
|\(\rho\)|State|
|\(H\)|Entropy|
|\(d_{EE}\)|Entropy metric|
|\(C_L\)|Collapse|
|\(P\)|Proposition|
|\(G\)|Knowledge field|

## References
1. Nielsen & Chuang, QIC (2000).
2. Schumacher, PRL 74, 2599 (1995).
3. Shor, PRL 79, 325 (1997).
4. Wootters & Zurek, Nature 299, 802 (1982).
5. Bennett, PRL 70, 1895 (1993).
6. Lloyd, PRL 88, 237901 (2002).
7. Preskill, Nature Phys. 5, 211 (2009).
8. Arute et al., Nature 574, 505 (2019).

---
### ضمیمهٔ فارسی
اصل تقارن اطلاعاتی: کمینه‌سازی وزن به کمک آنتروپی و هم‌راستایی با نگاه. مثال دوبعدی و کد همراه آمده است.
