# Entropy Lemma

## Preliminaries
- Hilbert space \(\mathcal H = \mathbb C^n\).
- State \(|\psi\rangle \in \mathcal H\), normalized: \(\langle\psi|\psi\rangle=1\).
- Probabilities: \(p_i = |\psi_i|^2\).
- Entropy: \(H(\psi) = -\sum_i p_i \log p_i\).
- Collapse: \(C(\psi) = e_k\) with probability \(p_k\), \(e_k\) basis vector.

## Lemma 1 (Necessity)
اگر جفت \(|\psi\rangle,|\phi\rangle\) تقارن اطلاعاتی داشته باشد،
\[
H(\psi)=H(\phi)=\ln 2
\]
اثبات: آنتروپی یکنواخت در بُعد ۲ لازم است.

## Lemma 2 (Sufficiency)
اگر \(|\psi\rangle\) طوری باشد که
\[
H(\psi)=\ln 2,
\]
پس وزن اطلاعاتی یکنواخت و تقارن برقرار می‌شود.

## Example
\[
|\psi\rangle=\tfrac{1}{\sqrt2}(1,1),\quad
|\phi\rangle=\tfrac{1}{\sqrt2}(1,-1)
\]
محاسبه:
\[
H(\psi)=H(\phi)=-2(\tfrac12\ln\tfrac12)=\ln2.
\]

## Discussion
تقارن آنتروپی \(H=\ln2\) حالتی دوجهتی را در تراز «فعال/غیرفعال» نگاه مدل می‌کند؛ هر کدام به احتمال برابر فعال می‌شوند.
