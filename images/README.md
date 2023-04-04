
# Heart Disease Prediction using Neural Networks

Cardiovascular disease prediction aids practitioners in making more accurate health decisions for their patients. Early detection can aid people in making lifestyle changes and, if necessary, ensuring effective medical care


## Authors

- [@chandrashekhar G T](https://www.github.com/chandugt35295)


## Usage/Examples
import pandas as pd
df =pd.read_csc(r'file.csv')

## Related

Here are some related projects

[Awesome README](https://github.com/matiassingers/awesome-readme)


## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)


## Documentation

Understanding columns in Dataset
Age:
Age of person in Years
Sex:
Male(1),Female(0)
Cp: Chest Pain
Value 0: asymptomatic(Silent (asymptomatic) myocardial ischemia (SMI) is defined as a transient alteration in myocardial perfusion in the absence of chest pain or the usual anginal equivalents.)
Value 1: atypical angina(Atypical pain is frequently defined as epigastric or back pain or pain that is described as burning, stabbing, or characteristic of indigestion. Typical symptoms usually include chest, arm, or jaw pain described as dull, heavy, tight, or crushing)
Value 2: non-anginal pain(A chest pain is very likely nonanginal if its duration is over 30 minutes or less than 5 seconds, it increases with inspiration, can be brought on with one movement of the trunk or arm, can be brought on by local fingers pressure, or bending forward, or it can be relieved immediately on lying down.)
Value 3: typical angina(Angina is a type of chest pain caused by reduced blood flow to the heart. Angina is a symptom of coronary artery disease. Angina is also called angina pectoris. Angina pain is often described as squeezing, pressure, heaviness, tightness or pain in the chest.)
trestbps:
The person's resting blood pressure (mm Hg on admission to the hospital)
chol:
Blood cholesterol is a waxy, fat-like substance made by your liver. Blood cholesterol is essential for good health. Your body needs it to perform important jobs, such as making hormones and digesting fatty foods.The person's cholesterol measurement in mg/dl.
fbs:
This measures your blood sugar after an overnight fast (not eating). A fasting blood sugar level of 99 mg/dL or lower is normal, 100 to 125 mg/dL indicates you have prediabetes, and 126 mg/dL or higher indicates you have diabetes.(> 120 mg/dl, 1 = True; 0 = False)
restecg:Resting Electrocardiographic Results
Value 0: showing probable or definite left ventricular hypertrophy by Estes’ criteria
Value 1: normal
Value 2: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)
thalach:
The person's maximum heart rate achieved.
exang:
Exercise induced angina Warm-up angina is a common and intriguing phenomenon in which, in subjects with ischemic heart disease, angina induced by initial exercise is attenuated or even disappears if they briefly slacken or interrupt their exertion before resuming it at the same or even greater level of intensity,(1 = yes; 0 = no)
oldpeak:
ST depression induced by exercise relative to rest ('ST' relates to positions on the ECG plot. See more here) slope: the slope of the peak exercise ST segment — 0: downsloping; 1: flat; 2: upsloping. 0: downsloping; 1: flat; 2: upsloping.
slope:
The slope of the peak exercise ST segment — 0: downsloping; 1: flat; 2: upsloping
ca:
Number of major vessels (0–3) colored by flourosopy,measured in intervals
thal:
Thalassemia (thal-uh-SEE-me-uh) is an inherited blood disorder that causes your body to have less hemoglobin than normal. Hemoglobin enables red blood cells to carry oxygen. Thalassemia can cause anemia, leaving you fatigued.
Value 1: fixed defect (no blood flow in some part of the heart)
Value 2: normal blood flow
Value 3: reversible defect (a blood flow is observed but it is not normal)
target:
Heart disease (1 = yes, 0= no)

