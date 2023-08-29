import numpy as np
import pandas as pd
import streamlit as st


def primeFactors(n):
    prime_factors = lambda n: [i for i in range(2, n+1) if n%i == 0 and all(i % j != 0 for j in range(2, int(i**0.5)+1))]
    factors = []
    while n > 1:
        for factor in prime_factors(n):
            factors.append(factor)
            n //= factor
    return factors 

def create_prime_exponet_series(m):
    prime_exponet_series = pd.Series(primeFactors(m)).value_counts()
    return(prime_exponet_series)

def uniquePrimeFactors(k):
    unique_factors = np.unique(primeFactors(k))
    return unique_factors.tolist()


input_numbers = st.text_input("Enter any number of integers (seperated by comma)")
numbers  = input_numbers.split(",")
numbers = [x.strip() for x in numbers]


if input_numbers:
    
    numbers = list(map(int, numbers))

    shared_prime_factors = []
    list_of_combined_prime_exponent_series = []

    for i in numbers:
        
        base_exp_ltx = f'''{i} = '''
        for base, exp in create_prime_exponet_series(i).items():
            base_exp_ltx += f'''{base}^{int(exp)} ×'''
        
        base_exp_ltx = base_exp_ltx[:-1]
        st.latex(base_exp_ltx)

        shared_prime_factors = (shared_prime_factors + uniquePrimeFactors(i))
        list_of_combined_prime_exponent_series.append(create_prime_exponet_series(i))
        combined_prime_exponent_df = pd.concat(list_of_combined_prime_exponent_series, axis=1)

    unique_shared_prime_factors = np.unique(shared_prime_factors)
    combined_prime_exponent_df["max"] = np.nanmax(combined_prime_exponent_df, axis=1)

    lcm = int(np.power(combined_prime_exponent_df.index, combined_prime_exponent_df["max"]).prod())

    
    b_e_ltx = '''LCM = '''
    for b, e in zip(combined_prime_exponent_df.index, combined_prime_exponent_df["max"]):
        b_e_ltx += f'''{b}^{int(e)} ×'''
    
    b_e_ltx = b_e_ltx[:-1] + f'= {lcm}'
    
    st.latex(b_e_ltx)
    
    
 