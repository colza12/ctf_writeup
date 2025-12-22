.class public Lcom/hellocmu/picoctf/FlagstaffHill;
.super Ljava/lang/Object;
.source "FlagstaffHill.java"


# direct methods
.method public constructor <init>()V
    .locals 0

    .line 6
    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method

.method public static getFlag(Ljava/lang/String;Landroid/content/Context;)Ljava/lang/String;
    .locals 10
    .param p0, "input"    # Ljava/lang/String;
    .param p1, "ctx"    # Landroid/content/Context;

    .line 11
    const/4 v0, 0x6

    new-array v0, v0, [Ljava/lang/String;

    .line 12
    .local v0, "witches":[Ljava/lang/String;
    const/4 v1, 0x0

    const-string v2, "weatherwax"

    aput-object v2, v0, v1

    .line 13
    const/4 v1, 0x1

    const-string v2, "ogg"

    aput-object v2, v0, v1

    .line 14
    const/4 v1, 0x2

    const-string v2, "garlick"

    aput-object v2, v0, v1

    .line 15
    const/4 v1, 0x3

    const-string v2, "nitt"

    aput-object v2, v0, v1

    .line 16
    const/4 v1, 0x4

    const-string v2, "aching"

    aput-object v2, v0, v1

    .line 17
    const/4 v1, 0x5

    const-string v2, "dismass"

    aput-object v2, v0, v1

    .line 19
    const/4 v1, 0x3

    .line 20
    .local v1, "first":I
    sub-int v2, v1, v1

    .line 21
    .local v2, "second":I
    div-int v3, v1, v1

    add-int/2addr v3, v2

    .line 22
    .local v3, "third":I
    add-int v4, v3, v3

    sub-int/2addr v4, v2

    .line 23
    .local v4, "fourth":I
    add-int v5, v1, v4

    .line 24
    .local v5, "fifth":I
    add-int v6, v5, v2

    sub-int/2addr v6, v3

    .line 26
    .local v6, "sixth":I
    aget-object v7, v0, v5

    .line 27
    const-string v8, ""

    invoke-virtual {v8, v7}, Ljava/lang/String;->concat(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v7

    const-string v8, "."

    invoke-virtual {v7, v8}, Ljava/lang/String;->concat(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v7

    aget-object v9, v0, v3

    invoke-virtual {v7, v9}, Ljava/lang/String;->concat(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v7

    invoke-virtual {v7, v8}, Ljava/lang/String;->concat(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v7

    aget-object v9, v0, v2

    .line 28
    invoke-virtual {v7, v9}, Ljava/lang/String;->concat(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v7

    invoke-virtual {v7, v8}, Ljava/lang/String;->concat(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v7

    aget-object v9, v0, v6

    invoke-virtual {v7, v9}, Ljava/lang/String;->concat(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v7

    invoke-virtual {v7, v8}, Ljava/lang/String;->concat(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v7

    aget-object v9, v0, v1

    .line 29
    invoke-virtual {v7, v9}, Ljava/lang/String;->concat(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v7

    invoke-virtual {v7, v8}, Ljava/lang/String;->concat(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v7

    aget-object v8, v0, v4

    invoke-virtual {v7, v8}, Ljava/lang/String;->concat(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v7

    .line 32
    .local v7, "password":Ljava/lang/String;
    invoke-virtual {p0, v7}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v8

    if-eqz v8, :cond_0

    invoke-static {p0}, Lcom/hellocmu/picoctf/FlagstaffHill;->sesame(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v8

    return-object v8

    .line 33
    :cond_0
    const-string v8, "NOPE"

    return-object v8
.end method

.method public static native sesame(Ljava/lang/String;)Ljava/lang/String;
.end method
