res = {}
__src = {}
__var = {"map-node": {"direct": "DIRECT", "reject": "REJECT"}, "rex": []}


def let(lsrc: dict) -> None:
    global __src
    __src = lsrc
    for item in __src["node"]:
        if "id" in item:
            __var["map-node"][item["id"]] = item["name"]


def profile(out) -> None:
    global res
    res = [
        "[General]",
        # "resource-parser = " + loc["parse"],
        # "internet-test-url = " + __src["misc"]["test"],
        "proxy-test-url = " + __src["misc"]["test"],
    ]
    if "dns" in __src["misc"]:
        res.append("dns-server = " + ", ".join(__src["misc"]["dns"]))
    if "doh" in __src["misc"]:
        res.append("doh-server = " + ", ".join(__src["misc"]["doh"]))
    if "dot" in __src["misc"]:
        res.append("dot-server = " + ", ".join(__src["misc"]["dot"]))

    res.append("\n[Mitm]")

    res.append("\n[Proxy]")

    res.append("\n[Proxy Chain]")

    res.append("\n[Proxy Group]")
    tmp_idx_reg = 0
    for item in __src["node"]:
        line = item["name"]
        if item["type"] == "static":
            line += " = select"
        elif item["type"] == "test":
            line += " = url-test"
        else:
            continue
        if "list" in item:
            for val in item["list"]:
                if val[0] == "-":
                    line += ", " + __var["map-node"][val[1:]]
                else:
                    line += ", " + val
        if "regx" in item:
            line += ", Rex" + str(tmp_idx_reg)
            tmp_idx_reg += 1
        if item["type"] == "test":
            line += ", url=" + __src["misc"]["test"] + ", interval=600"
        if "icon" in item:
            line += ", img-url=" + item["icon"]["sf"][:-7]
        res.append(line)

    res.append("\n[Rule]")
    res.append("FINAL, " + __var["map-node"][__src["filter"]["main"]])

    res.append("\n[Remote Proxy]")
    res.extend(
        [
            "Proxy" + str(idx) + " = " + item + ", parser-enabled=true, enabled=true"
            for idx, item in enumerate(__src["proxy"]["link"])
        ]
    )

    res.append("\n[Remote Filter]")
    __var["rex"] = [item["regx"] for item in __src["node"] if "regx" in item]
    res.extend(
        [
            "Rex" + str(idx) + ' = NameRegex, FilterKey="' + item + '"'
            for idx, item in enumerate(__var["rex"])
        ]
    )

    res.append("\n[Remote Rule]")
    res.extend(
        [
            (
                item[2]
                + ", tag=DN"
                + item[1]
                + ", policy="
                + __var["map-node"][item[3]]
                + ", parser-enabled=true, enabled=true"
            )
            for item in __src["filter"]["dn"]["surge"]
            if item[0] in set([1, 2])
        ]
        + [
            (
                item[2]
                + ", tag=IP"
                + item[1]
                + ", policy="
                + __var["map-node"][item[3]]
                + ", parser-enabled=true, enabled=true"
            )
            for item in __src["filter"]["ip"]["surge"]
            if item[0] == 1
        ]
    )

    out.writelines([x + "\n" for x in res])
