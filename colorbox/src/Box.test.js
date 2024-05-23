import React from "react";
import { render } from "@testing-library/react";

import Box from "./Box";

it("renders without crashing", function () {
    render(<Box />);
    }
);  

it("matches snapshot", function () {
    const { asFragment } = render(<Box />);
    expect(asFragment()).toMatchSnapshot();
    }
);

it("matches snapshot with props", function () {
    const { asFragment } = render(<Box id={1} width={5} height={5} backgroundColor="blue" />);
    expect(asFragment()).toMatchSnapshot();
    }
);