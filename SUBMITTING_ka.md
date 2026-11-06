# როგორ გავაგზავნოთ — Pull Request-ით

ეს არასდროს გაგიკეთებიათ და არაუშავს — ყველა ნაბიჯი აქ არის. **Fork**
არის ამ რეპოზიტორის თქვენი საკუთარი ასლი GitHub-ზე. **Branch** არის
ადგილი, სადაც თქვენი ცვლილებები ინახება. **Pull Request (PR)** სთხოვს
თქვენი branch-ის ცვლილებების შერწყმას ორიგინალ რეპოზიტორთან.

> ყველგან, სადაც ხედავთ `<your-username>`-ს, ჩაანაცვლეთ ის — კუთხოვანი
> ფრჩხილების ჩათვლით — თქვენი რეალური GitHub username-ით. `<your-username>`-ის
> სიტყვასიტყვით აკრეფა ბრძანებაში არ იმუშავებს.

## 1. დააინსტალირეთ Git

- **Windows:** დააინსტალირეთ [Git for Windows](https://git-scm.com/download/win). გამოიყენეთ "Git Bash" ტერმინალად შემდეგი ნაბიჯებისთვის.
- **macOS:** გახსენით Terminal და გაუშვით `git --version` — თუ არ არის დაინსტალირებული, macOS შემოგთავაზებთ დაინსტალირებას.
- **Linux:** `sudo apt install git` (Debian/Ubuntu) ან თქვენი დისტრიბუტივის პაკეტების მენეჯერი.

დარწმუნდით რომ იმუშავა:
```
git --version
```

## 2. შექმენით GitHub ანგარიში

თუ არ გაქვთ, დარეგისტრირდით [github.com](https://github.com)-ზე.

## 3. დააკონფიგურირეთ Git თქვენი სახელით და ელფოსტით

```
git config --global user.name "თქვენი სახელი"
git config --global user.email "you@example.com"
```

## 4. მოაწყვეთ შესვლის (sign-in) მეთოდი

პირველი push-ი (მე-10 ნაბიჯში) მოგთხოვთ დამტკიცებას, რომ ეს მართლა
თქვენ ხართ. მოაწყვეთ ეს ახლა, რომ მოგვიანებით არ გაგიკვირდეთ.

- **Windows:** Git for Windows შეიცავს Git Credential Manager-ს. პირველი
  push-ისას გაიხსნება ბრაუზერის ჩანართი — შედით იქ GitHub-ზე და
  დაადასტურეთ. ამის შემდეგ Git დაიმახსოვრებს თქვენ.
- **macOS / Linux:** GitHub-მა შეწყვიტა ანგარიშის პაროლის მიღება
  `git push`-ისთვის. უმარტივესი გამოსავალია [GitHub CLI](https://cli.github.com/):
  დააინსტალირეთ და გაუშვით:
  ```
  gh auth login
  ```
  აირჩიეთ **GitHub.com**, **HTTPS**, და **Login with a web browser**,
  შემდეგ მიჰყევით ინსტრუქციებს. ეს ასევე დააფიქსირებს თქვენს
  შესვლას მომავალი push-ებისთვის.

## 5. Fork-ი გაუკეთეთ ამ რეპოზიტორს

გადადით ამ რეპოზიტორის GitHub გვერდზე —
`https://github.com/PythonADI/python-127-homework-8` — და დააჭირეთ
**Fork**-ს (ზედა მარჯვენა კუთხეში). გამოიყენეთ ნაგულისხმევი
პარამეტრები. ეს შექმნის თქვენს საკუთარ ასლს:
`https://github.com/<your-username>/python-127-homework-8`.

## 6. Clone გაუკეთეთ თქვენს fork-ს

```
git clone https://github.com/<your-username>/python-127-homework-8.git
cd python-127-homework-8
```

## 7. შექმენით branch თქვენი GitHub username-ის სახელით

```
git checkout -b <your-username>
```

მოსალოდნელი შედეგი: `Switched to a new branch '<your-username>'`.

## 8. შექმენით თქვენი საქაღალდე და დაამატეთ ფაილები

შექმენით საქაღალდე `submissions/`-ის შიგნით, დასახელებული თქვენი
GitHub username-ით:

```
mkdir -p submissions/<your-username>
```

შემდეგ ჩადეთ იქ თქვენი სავარჯიშოების ფაილები, რომ საბოლოოდ გქონდეთ:

```
submissions/<your-username>/exercise_1.py
submissions/<your-username>/exercise_2.py
submissions/<your-username>/exercise_3.py
submissions/<your-username>/exercise_4.py
submissions/<your-username>/exercise_5.py
```

**მხოლოდ თქვენი საკუთარი საქაღალდე.** არ შეცვალოთ `README.md`,
`EXERCISES.md`, `SUBMITTING.md`, ან სხვა სტუდენტის საქაღალდე.

## 9. გაუშვით ყველა ფაილი commit-მდე

- **Windows:** `py submissions/<your-username>/exercise_1.py` (თუ
  უბრალო `python` არ მუშაობს ან Microsoft Store-ს ხსნის, გამოიყენეთ
  `py`).
- **macOS / Linux:** `python3 submissions/<your-username>/exercise_1.py`.

შეადარეთ შედეგი იმას, რასაც `EXERCISES.md` ამბობს — უნდა ემთხვეოდეს
ზუსტად.

## 10. Commit და push გაუკეთეთ თქვენს branch-ს

```
git add submissions/<your-username>
git commit -m "Add homework 8"
git push -u origin <your-username>
```

თუ ეს თქვენი პირველი push-ია, მოგთხოვთ შესვლას (იხილეთ მე-4 ნაბიჯი) —
მიჰყევით მითითებას, შემდეგ push დასრულდება.

## 11. გახსენით Pull Request

GitHub push-ის შემდეგ დაბეჭდავს ბმულს, ასევე გამოჩნდება
"Compare & pull request" ბანერი თქვენი fork-ის გვერდზე — დააჭირეთ
რომელიმეს. ან გახსენით ერთი ხელით
`https://github.com/PythonADI/python-127-homework-8/compare`-დან:

- **base repository:** `PythonADI/python-127-homework-8`, branch `main`
- **head repository:** `<your-username>/python-127-homework-8`, branch `<your-username>`

**სათაური:** `Homework 8 - თქვენი სახელი` (თქვენი რეალური სახელი).

შეავსეთ checklist PR-ის აღწერაში, შემდეგ დააჭირეთ
**Create pull request**-ს (არა "Create draft pull request").

## 12. დაელოდეთ განხილვას

თქვენ არ გაქვთ write წვდომა ორიგინალ რეპოზიტორზე, ამიტომ ვერ
დააგზავნით პირდაპირ — მხოლოდ Pull Request-ს შეუძლია თქვენი
ცვლილებების შეტანა. ინსტრუქტორი ავტომატურად ემატება როგორც
reviewer.

თუ ცვლილებებს მოითხოვენ, გააკეთეთ ისინი იმავე branch-ზე და
თავიდან push გაუკეთეთ:

```
git add submissions/<your-username>
git commit -m "Address review feedback"
git push
```

არ გახსნათ მეორე PR — ეს ავტომატურად განახლდება.
