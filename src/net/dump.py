from ..lib import net
from . import ren
from .dumps import clash, clash_conv, conv, quantumult, shadowrocket, surge

# Var
__src = {}
__var = {"once": set()}


# Init
def init() -> None:
    ren.PATH_OUT.mkdir(parents=True, exist_ok=True)
    ren.PATH_OUT_SURGE.mkdir(parents=True, exist_ok=True)
    ren.PATH_OUT_CLASH.mkdir(parents=True, exist_ok=True)


def dump(lsrc: dict) -> None:
    global __src
    if not "ref" in lsrc:
        return
    var = lsrc.pop("ref")
    if var["id"] != "":
        var["id"] = "+" + var["id"]
    __src = lsrc

    if "quantumult" in var["tar"]:
        __quantumult(var["id"])
    if "clash" in var["tar"]:
        __clash(var["id"])
    if "surge" in var["tar"]:
        __surge(var["id"])
    if "shadowrocket" in var["tar"]:
        __shadowrocket(var["id"])


def __quantumult(alia: str) -> None:
    quantumult.let(__src)

    with open(
        ren.PATH_OUT / ("quantumult" + alia + ".conf"),
        "tw",
        encoding="utf-8",
    ) as out:
        quantumult.profile(
            out,
            {
                "parse": ren.URI_NET + "quantumult-parser.js",
            },
        )

    if not "qp" in __var["once"]:
        __var["once"].add("qp")
        net.download(
            ren.EXT_QUANTUMULT_PARSER,
            ren.PATH_OUT / "quantumult-parser.js",
        )


def __clash(alia: str) -> None:
    clash.let(__src)

    with open(
        ren.PATH_OUT_CLASH / ("profile" + alia + ".yml"), "tw", encoding="utf-8"
    ) as out:
        clash.config(out)

    clash_conv.let(__src)

    with open(
        ren.PATH_OUT_CLASH / ("conv" + alia + ".conf"),
        "tw",
        encoding="utf-8",
    ) as out:
        clash_conv.config(out, {"yml": ren.URI_CLASH + "conv-base" + alia + ".yml"})

    with open(
        ren.PATH_OUT_CLASH / ("conv-base" + alia + ".yml"),
        "tw",
        encoding="utf-8",
    ) as out:
        clash_conv.base(out)


def __surge(alia: str) -> None:
    surge.let(__src)

    with open(
        ren.PATH_OUT_SURGE / ("base" + alia + ".conf"),
        "tw",
        encoding="utf-8",
    ) as out:
        surge.base(out, {"up": ren.URI_SURGE + "base" + alia + ".conf"})

    if not "sp" in __var["once"]:
        __var["once"].add("sp")
        with open(
            ren.PATH_OUT_SURGE / "proxy.conf",
            "tw",
            encoding="utf-8",
        ) as out:
            surge.proxy(out)

    with open(
        ren.PATH_OUT_SURGE / ("profile" + alia + ".conf"),
        "tw",
        encoding="utf-8",
    ) as out:
        surge.profile(out, {"base": "base" + alia + ".conf"})

    if not "sc" in __var["once"]:
        __var["once"].add("sc")
        with open(
            ren.PATH_OUT / "conv.conf",
            "tw",
            encoding="utf-8",
        ) as out:
            conv.proxy(out)


def __shadowrocket(alia: str) -> None:
    shadowrocket.let(__src)

    with open(
        ren.PATH_OUT / ("shadowrocket" + alia + ".conf"),
        "tw",
        encoding="utf-8",
    ) as out:
        shadowrocket.config(
            out,
            {
                "up": ren.URI_NET + "shadowrocket" + alia + ".conf",
            },
        )
