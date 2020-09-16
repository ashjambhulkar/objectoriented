single = {
    b: {value: 23, next: c},
    c: {value: 34, next: d},
    d: {value: 46, next: e},
    e: {value: 25, next: f},
    a: {value: 59, next: b}
}


double = {
    b: {value: 23, next: c, prev: a},
    e: {value: 25, next: f, prev: d},
    a: {value: 59, next: b, prev: None},
    b: {value: 49, next: c, prev: a}
}
