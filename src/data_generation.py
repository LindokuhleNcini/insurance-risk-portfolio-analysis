import numpy as np
import pandas as pd

def generate_portfolio(n_policies=1000, seed=42):
    np.random.seed(seed)
    policy_id = np.arange(1, n_policies + 1)
    exposure = np.random.uniform(5000, 50000, n_policies)
    loss_prob = np.random.beta(2, 20, n_policies)
    losses = exposure * loss_prob
    df = pd.DataFrame({
        "policy_id": policy_id,
        "exposure": exposure,
        "loss_prob": loss_prob,
        "losses": losses
    })
    df.to_csv("../data/insurance_portfolio.csv", index=False)
    print("Portfolio generated and saved to data/insurance_portfolio.csv")
    return df

if __name__ == "__main__":
    generate_portfolio()