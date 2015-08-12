# Trans4mers


Trans4mers is a sklearn compatible python package that implements some methods
of data preprocessing. Currently the methods implemented are:

- Imputation:
  - KNN Regression: This method imput values for missing values based on KNN
  Regression.
- Feature Extraction: I'm not sure if the above methods are really feature
extractors.
  - Hyberbolic Location Fingerprint: This method is used on Indoor Wifi
  Localization when there are heterogeneous devices environment. For more
  details: M. Kjaergaard and C. Munk, "Hyperbolic Location Fingerprint: A
  calibration-free solution for handling differences in signal strength",
  in PerCom, pp. 110-116, 2008
  - Relative Location Fingerprint: This method is just a variation of the above.
  Instead of use Hyberbolic tranformation it just take the relation betwee two
  variables.
- Normalization:
  - Standard Normalization: This method normalize each row of a dataset based
  on the mean and standard variation among the variables of the row.


## Instaling

First clone the repository to your machine:

```bash
git clone git@github.com:rloliveirajr/sklearn_transformers.git
```

Then, install the package using pip or easy_install:

```bash
pip setup.py install
```

## Using
...

## Contributions

Any contribution is welcome!


