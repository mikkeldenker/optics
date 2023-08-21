import pandas as pd

# csv source: https://github.com/maltfield/awesome-lemmy-instances
df = pd.read_csv("awesome-lemmy-instances.csv")

instances = df["Instance"].tolist()

# hacky but works
urls = [instance.split("](")[1][:-1] for instance in instances]
sites = [url.split("//")[1].split("/")[0] for url in urls]


def rule(site):
    s = """Rule {{
    Matches {{
        Site("|{0}|"),
        Ulr("post"),
    }}
}};""".format(
        site
    )

    return s


print("// source of instances: https://github.com/maltfield/awesome-lemmy-instances")
print("DiscardNonMatching;")
print()
print("\n\n".join([rule(site) for site in sites]))
