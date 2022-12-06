const characters = [
    {
        name: 'Luke Skywalker',
        height: '172',
        mass: '77',
        eye_color: 'blue',
        gender: 'male',
    },
    {
        name: 'Darth Vader',
        height: '202',
        mass: '136',
        eye_color: 'yellow',
        gender: 'male',
    },
    {
        name: 'Leia Organa',
        height: '150',
        mass: '49',
        eye_color: 'brown',
        gender: 'female',
    },
    {
        name: 'Anakin Skywalker',
        height: '188',
        mass: '84',
        eye_color: 'blue',
        gender: 'male',
    },
];

const names = characters.map((character) => character.name);
console.log(names);

const heights = characters.map((character) => character.height);
console.log(heights)

const minifiedRecords = characters.map((character) => ({
    name: character.name,
    height: character.height,
}));
console.log(minifiedRecords);

const firstNames = characters.map((character) =>character.name.split(' ')[0]);
console.log(firstNames);