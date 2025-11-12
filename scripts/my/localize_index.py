import pandas as pd


def match_tz(df, tz):
    index = pd.date_range(
        start=df.index.min(),
        end=df.index.max(),
        freq="h",
        tz=tz,
        name=df.index.name,
    ).tz_localize(tz=None)
    df = df.reindex(index=index)
    df = df.tz_localize(
        tz=tz,
        ambiguous="infer",
    )
    return df


def main():
    est_to_dst = "2024-03-31"
    dst_to_est = "2024-10-27"
    data = range(1, 25)
    est_to_dst_index = pd.date_range(
        start=pd.Timestamp(est_to_dst),
        end=pd.Timestamp(est_to_dst) + pd.DateOffset(),
        freq="h",
        inclusive="left",
    )
    dst_to_est_index = pd.date_range(
        start=pd.Timestamp(dst_to_est),
        end=pd.Timestamp(dst_to_est) + pd.DateOffset(),
        freq="h",
        inclusive="left",
    )
    est_to_dst_naive = pd.DataFrame(data=data, index=est_to_dst_index)
    dst_to_est_naive = pd.DataFrame(data=data, index=dst_to_est_index)

    est_to_dst_aware = match_tz(est_to_dst_naive, "Europe/Warsaw")
    dst_to_est_aware = match_tz(dst_to_est_naive, "Europe/Warsaw")


if __name__ == "__main__":
    main()
