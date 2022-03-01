# CSS(Cascading Style Sheets)

**CSS**는 HTML의 요소의 모양을 정의하여 어떻게 화면에 렌더링할 것인지 브라우저에게 설명하는 언어이다.

**HTML5** 이전에도 style 정의가 가능한 태그(`<font>`, `<center>` 등)가 존재하였으나, 내용(content)와 구조(structure)라는 HTML 본연의 기능과 동떨어진 탓에 혼란만 가중되었다. 그에 따라 **HTML5**부터는 각각의 기능에 충실하는 언어로 확실히 구분되었다. **HTML**은 *정보*와 *구조화*를, **CSS**는 *style 정의*를 담당한다.

현재 **CSS**의 버전은 **CSS3**이다.

## CSS 문법

CSS의 전체 구조를 **rule set(이하 rule)**이라고 한다. 그 안에는 각각 역할에 대한 명칭이 있다.

[MDN에서 퍼온 rule set 이미지]("https://mdn.mozillademos.org/files/9461/css-declaration-small.png")

### (1) 셀렉터(Selector, 선택자)

**rule**의 맨 앞에 있는 것으로, **HTML** 요소를 선택한다. **셀렉터**를 통해 다른 요소를 꾸밀 수 있다.

### (2) 프로퍼티(Property, 속성)와 값(Value, 속성값)

꾸밀 요소를 선택한 후 _중괄호{ }_ 내에 **프로퍼티**와 **값**을 지정하는 것으로 style을 정의할 수 있다. CSS 규칙에 따라 **프로퍼티**를 사용하여야 하며, **값**은 해당 **프로퍼티**가 사용할 수 있는 _키워드_ 혹은 *특정 단위*를 지정해야 한다. 여러 개의 **프로퍼티**는 *세미콜론(;)*으로 구분한다.

### (3) HTML과 CSS 연결

HTML과 CSS는 `<head>`의 `<link>`로 연결해 로드한다.

```html
<!DOCTYPE html>
<html>
  <head>
    <link rel="stylesheet" href="css/style.css" />
  </head>
  <body>
    <h1>Hello World</h1>
    <p>This is a web page.</p>
  </body>
</html>
```

```css
h1 {
  color: red;
}
p {
  background: blue;
}
```

이러한 방식을 **Link style**이라고 부른다. 하지만 필수적인 사용법은 아니며, 다른 두 가지 방식이 더 있다.

```html
<!DOCTYPE html>
<html>
  <head>
    <style>
      h1 {
        color: red;
      }
      p {
        background: aqua;
      }
    </style>
  </head>
  <body>
    <h1>Hello World</h1>
    <p>This is a web page.</p>
  </body>
</html>
```

먼저 css 파일을 만들지 않고 `<style>`태그를 통해 문서 내에서 정의하는 방식인 **Embedding style**이다. 꼭 `<head>`가 아니어도 사용할 수 있다.

```html
<!DOCTYPE html>
<html>
  <head> </head>
  <body>
    <h1>Hello World</h1>
    <p>This is a web page.</p>
    <style>
      h1 {
        color: red;
      }
      p {
        background: aqua;
      }
    </style>
  </body>
</html>
```

꾸미고 싶은 요소 주변에 넣는 것도 가능하지만, 가독성이 떨어지고 유지보수가 쉽지 않다.

```html
<!DOCTYPE html>
<html>
  <body>
    <h1 style="color: red">Hello World</h1>
    <p style="background: aqua">This is a web page.</p>
  </body>
</html>
```

남은 하나는 **Inline style**이다. 문자 그대로 태그가 있는 line에 곧장 쑤셔 넣는 방법이다. 가장 강력한 style 정의지만, 역시 가독성이 나쁘고 유지보수가 어렵다.

셋 중 가장 보편적인 방법은 **Link style**이다. **HTML**과 **CSS**의 역할이 다르기 때문에 다른 파일로 구분하여 작성하고 관리하는 것이 바람직하다.

### (4) Reset CSS

모든 웹 브라우저는 기본 스타일을 가지고 있어 CSS가 없어도 작동하지만, 기본 스타일과 지원하는 tag, style도 제각각이다. 이런 문제점을 하나의 스타일로 통일시켜주는 역할이 **Reset CSS**이다. 자주 사용하는 **Reset CSS**는 [Eric Meyer’s reset](https://meyerweb.com/eric/tools/css/reset/)와 [normalize.css](https://necolas.github.io/normalize.css/)가 있다.
