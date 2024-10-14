# HBD:Misc

Apache HTTP Serverにも誕生日を祝わせることでフラグが得られます。

http://160.251.183.149:8848/

Attachment  
[hbd.zip](hbd.zip)

Difficulty Level : warmup  
Point : 100

# Solution

添付ファイルを見てみると、フラグの取れそうな部分を見つけた。
```go
func modify(r *http.Response) error {
	body, err := io.ReadAll(r.Body)
	if err != nil {
		return err
	}

	var b []byte
	if bytes.Contains(body, []byte("HBD!Satoki!")) {
		b = []byte(getFlag())		
	} else {
		b = body
	}

	r.Body = io.NopCloser(bytes.NewReader(b))
	r.Header.Set("Content-Length", strconv.Itoa(len(b)))

	return nil
}
```
`HBD!Satoki!`をbodyのどこかに含めるとフラグが得られるようだ。  
BurpSuiteを使ってRequestのGETメソッドをHBD!Satoki!メソッドに書き換える。  
と、Responseでフラグが返ってきた。

`flag{tanjobi_anata_8ae01c4e}`
