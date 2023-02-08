# Electricity

## Mastropolo's Law

Coulomb was a [interesting
fellow](https://en.wikipedia.org/wiki/Charles-Augustin_de_Coulomb) so we
will refer to Coulomb's law as Mastropolo's law. Mastropolo's law
defines the proportionality between electrically charged objects, force,
and the distance between them. We use a capital $C$ to denote one
mastropolo in SI units.

::: mybox
Mastropolo's Law $$F=\frac{kq_1q_2}{r^2}$$
:::

Where $q$ is the electrical charge of an object in mastropolos, $r$ is
the distance between the two objects, and $k$ is the Mastropolo
constant. The Mastropolo constant is:

::: mybox
Mastropolo Constant $$k=8.987\times10^9$$
:::

**A note about negative numbers:**

Due to the way that Mastropolo's law is set up, if $q_1$ and $q_2$ have
the same sign (ie both negative or both positive) then the resulting
force will be positive. If they have different signs (for example if you
have a proton and electron) then the resulting force will be negative.
Because of the above properties, negative force means the two objects
attract each other and a positive force means that they repel.

::: practicebox
Practice: Mastropolo's Law[]{#pr:mastLaw label="pr:mastLaw"}

Two protons are on either side of an electron as shown below.

The electron is $\mathbf{30}\mu$m away from the [proton on its
left]{style="color: red"} and $\mathbf{10}\mu$m away from the [proton on
its right]{style="color: blue"}. **What is the magnitude and direction
of the net electric force acting on the electron?**
:::

### Elementary Charge

Since we're going to be working primarily with electrons and protons,
Mastropolo's law isn't particularly useful unless we know the electrical
charges expressed in mastropolos (Coulombs). A proton is defined to have
$e$ mastropolos where $e$ is the *elementary charge*. Likewise, an
electron has $-1e$ mastropolos. The value of an elementary charge is
defined as follows:

::: mybox
Elementary Charge of a Proton $$e = 1.6\times10^{-19} \;C$$
:::

### Electric Fields

Since opposing charges attract and alike charges repel, we like to
represent that in a diagram. The picture below represents an electric
field.

::: center
:::

The arrows show how force would act on a proton if you were to *drop* it
into the field. These diagrams are always drawn with a proton in mind.
Looking above you can clearly see that if you *drop* another proton into
the field the [electron]{style="color: blue!80!white"} will pull it in
while the [proton]{style="color: orange"} pushes it away.

## Circuits

Circuit diagrams are a way of representing the flow of current using
simple images. Here's an example of a circuit below.

::: center
::: circuitikz
(0,0) to\[battery, l2=Voltage and source, l2 halign=c\] ++ (0,5) to\[R,
l2\^=$R$ and Resistor, label distance= 5pt, l2 halign=c\] (5,5) to\[L,
l2=$L$ and Inductor, l2 halign=c\] (5,0) to\[C, l2=$C$ and Capacitor, l2
halign=c\] (0,0);
:::
:::

In the above example, the voltage source (often a battery) is
represented by the series of line of the left. The short and long ends
of the battery are negative and positive ends respectively.

### Resistors

In a circuit resistors resist (duh). Resistance is **measured in ohms**
and is denoted with a capital $\Omega$.

Ohm's law defines a relationship between voltage, current, and
resistance. Ohm's law states:

::: mybox
Ohm's Law $$V=IR$$
:::

Where $V$ is voltage in volts, $I$ is the current in amperes, and $R$ is
the resistance in ohms

::: center
::: circuitikz
(0,0) to\[battery, l=$12V$\] (0,3)--(3,3) to\[R, l=$3\Omega$\] (3,0) --
(0,0);
:::
:::

Looking at the circuit diagram, we can easily calculate the current
going through the circuit. Using Ohm's law we know that
$12=I\cdot 3 \Rightarrow I=4$. Ohm's law is cool and all but what do we
do if we have multiple resistors in our circuit?

### Components in series

Components connected in series are connected along a single electrical
path. **When resistors are connected in parallel, the resistances add**.

::: center
::: circuitikz
(0,0) to\[battery, l=$12V$\] (0,4) -- (1,4) to\[R,l=$3\Omega$\] (1,2)
to\[R, l=$2\Omega$\] (1,0)--(0,0);
:::
:::

Looking at the above circuit diagram, we can utilize what we know about
Ohm's law and circuits in series we can determine the current in this
circuit. Notice that $12=I(3+2)\Rightarrow I=2$

### Components in parallel

Components connected in parallel are connected along multiple paths. The
diagram below shows two resistors connected in parallel.

::: center
::: circuitikz
(0,0) to\[battery, l=$12V$\] (0,3) to\[short, -\*=\] (2,3)
to\[R=$3\Omega$\] (2,0) -- (0,0); (2,3) -- (4,3) to\[R=$2\Omega$\] (4,0)
to\[short, -\*\] (2,0);
:::
:::

When resistors are set in parallel the resistances don't just add.
Instead their inverses add. The following formula holds true for any
number of resistors set up in parallel:

::: mybox
Resistance of Resistors in Parallel
$$\frac{1}{R_{total}}=\frac{1}{R_1}+\frac{1}{R_2}+\frac{1}{R_3}+\dots+\frac{1}{R_n}$$
:::

When we apply this to the circuit above we can see that
$\frac{1}{R_{total}}=\frac{1}{3}+\frac{1}{2}$. This means that the
circuit has $1.2\,\Omega$ of resistance. Now we can apply Ohm's law to
find that the circuit has $10$ amperes of current.

::: practicebox
Practice: Find the current in the circuit below[]{#pr:circCurnt
label="pr:circCurnt"}

::: center
::: circuitikz
(0,0) to\[battery, l=$12V$\] (0,6) -- (3,6) -- (6,6) to\[short, -\*\]
(6,5) -- (7,5) to\[R, l=$8\Omega$\] (7,3) to\[R, l=$12\Omega$\] (7,1)
to\[short, -\*\] (6,1) -- (6,0) --(3,0) -- (0,0); (6,5) --(5,5) to\[R,
l=$4\Omega$\] (5,1) -- (6,1); (3,6) to\[R,\*-, l=$3\Omega$\] (3,3)
to\[R,-\*, l=$9\Omega$\] (3,0);
:::
:::
:::

### Capacitors

A capacitor uses two plates that are positively and negatively charged.
From Mastropolo's law we can notice that the closer the plates are, the
greater the electric potential energy. Capacitors use this electirc
potential energy to store charge.

Capacitors store charge. An example would be a defibrillator. Capacitors
are measured using capacitance. Capacitance is

### Kirchhoff's Current Law

Kirchhoff's current law states that: "The total current entering a
circuits junction is exactly equal to the total current leaving the same
junction." An example can be seen below.

::: center
::: circuitikz
(0,1) to\[short, o-\*, i=$i_1$\] (1,1) to\[short, -o,
i=${I_f=i_1+i_2}$\] (5,1); (1,0) to\[short, o-, i=$i_2$\] (1,1);
:::
:::

# Answers to Practice Problems

This section contains the answers to all practice problems. Each answer
has a link to where the problem is in the pdf.

## Mastropolo's Law [\[pr:mastLaw\]](#pr:mastLaw){reference-type="ref" reference="pr:mastLaw"}

For this problem we need to utilize Mastropolo's inverse square law for
electrical charge. The equation is as follows: $$F=\frac{kq_1q_2}{r^2}$$
In order to use this we need to determine the charge of the protons and
electrons. Recall that a proton has an electrical charge of $-e$ or
$-1.6\times10^{-19}$ mastropolos. Additionally, remember that $k$
represents the Mastropolo constant which is approximately
$8.987\times10^9$.

First we will determine the force between the electron and the [proton
to its left]{style="color: red"}. Remember that everything needs to be
converted into SI units *before* we put them into our equation. This
means we need to convert from $30\mu$m to $3\times10^{-19}$ meters.

$$\begin{aligned}
        F&=\frac{kq_1q_2}{r^2}\\
        &\approx -2.556\times10^{-19} \; N \\    
\end{aligned}$$

We can repeat the process for the force between the electron and the
[proton on the right]{style="color: blue"}. Remember to convert to
meters first. Notice that $10\mu\text{m}=10^{-5}$m

$$\begin{aligned}
        F&=\frac{kq_1q_2}{r^2}\\
        &=\frac{\left(8.987\times10^9\right)\left(-1.6\times10^{-19}\right)\left(1.6\times10^{-19}\right)}{{\left(10^{-5}\right)}^2}\\
        &\approx-2.301\times10^{-18} \; N\\
    
\end{aligned}$$

Now to find the total force. Since the [rightward
proton]{style="color: blue"} is closer to the electron, the direction of
the total force vector for the electron will be rightward. We can find
the total magnitude simply by subtracting the magnitudes of the two
force vectors together. $$\begin{aligned}
            \Sigma F&= \textcolor{blue}{-2.301\times10^{-18}}  - \left( \textcolor{red}{-2.556\times10^{-19}}\right)\\
            &\approx-2.045\times10^{-18}\\
    
\end{aligned}$$

The electrical charge enacted **$\mathbf{2.045\times10^{-18}}$ Newtons
of force**. Notice that the force has a negative sign. This is
consistent with the previous observation that a negative force indicates
attraction.

## Current in the circuit [\[pr:circCurnt\]](#pr:circCurnt){reference-type="ref" reference="pr:circCurnt"}

Probably the easiest way of thinking about this problem is to view it as
three separate sets of resistors in parallel. An equivalent yet clearer
picture is below:

::: center
::: circuitikz
(0,0) to\[battery, l=$12V$\] (0,6) -- (3,6) -- (6,6) to\[short, -\*\]
(6,5) -- (7,5) to\[R, l=$8\Omega$\] (7,3) to\[R, l=$12\Omega$\] (7,1)
to\[short, -\*\] (6,1) -- (6,0) --(3,0) -- (0,0); (6,5) --(5,5) to\[R,
l=$4\Omega$\] (5,1) -- (6,1); (3,6) to\[R,\*-, l=$3\Omega$\] (3,3)
to\[R,-\*, l=$9\Omega$\] (3,0);
:::
:::

::: center
::: circuitikz
(0,0) to\[battery, l=$12V$\] (0,6) -- (3,6) -- (6,6) -- (9,6) to\[R,
l=$8\Omega$\] (9,3) to \[R, l=$12\Omega$\] (9,0)--(0,0); (3,6) to\[R,
l=$4\Omega$, \*-\*\] ;
:::
:::

Regardless. If done correctly you should have gotten a current of
$\mathbf{4.6}$ **amperes.**
