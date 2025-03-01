import { useEffect, useRef } from "react";

export const useFadeIn = (duration = 1, delay = 1) => {
    const element = useRef();
    useEffect(() => {
        if (typeof duration != "number" || typeof delay != "number") return;
        if (element.current) {
            const { current } = element;
            current.style.transition = `opacity ${duration}s ease-in-out ${delay}s`;
            current.style.opacity = 1;

            let span = document.createElement("span");
            span.innerText = `(duration${duration}s, delay${delay}s)`;
            current.appendChild(span);
        }
    }, []);
    return { ref: element, style: { opacity: 0 } }
};