from typing import Any, Dict, List, Optional, Tuple

import pandas as pd


# considerando que a tabela transactions campo AdressOrigin é responsável por pagar as taxas de envio,
# o campo totalSend tem que seguir o intervalo de valores entre o campos range-start e range-end para o campo fee-percentage da tabela fee,
# qual AdressOrigin seria responsável pelo maior pagamento de fee em janeiro de 2023?.

def load_data(CSV_URL: str) -> pd.DataFrame:
    """Loads transaction data from GitHub CSV."""
    try:
        df = pd.read_csv(CSV_URL, delimiter=";", encoding="utf-8")
        #df["transaction_date"] = pd.to_datetime(df["transaction_date"])
        return df
    except Exception as e:
        print(f"❌ Failed to load CSV: {e}")
        return pd.DataFrame()  # Return empty DataFrame on error
    

