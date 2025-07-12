const o = {
    prop: 100,
    f: function() {
        return this.prop;
    }
}
console.log(o.f());

const arrow = () => {console.log(this);};

const arrowThis = {
    prop: 100,
    f: function() {
        console.log(( ()=>this )());
    }
}

arrowThis.f();