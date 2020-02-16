# Problem_Solving_2020_Spring
bacteria_horizental_gene_transfer

## The Mathematical model of the system is shown below.
\begin{align}
&\frac{dR}{dt} = a_R R(1-\frac{R}{k_R} - \frac{S}{k_S} - \frac{M}{k_M}) \\
&\frac{dS}{dt} = a_S S(1-\frac{R}{k_R} - \frac{S}{k_S} - \frac{M}{k_M})-eSR-fSM \\
&\frac{dM}{dt} = a_M M(1-\frac{R}{k_R} - \frac{S}{k_S} - \frac{M}{k_M})+eSR+fSM
\end{align}

## Agent-based modeling using mesa+networkx in python
