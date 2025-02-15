from restack_ai.function import function, log
from pydantic import BaseModel


class Book1(BaseModel):
    chapter: str
    part: str
    content: str


@function.defn()
async def lookup_book() -> str:
    try:
        log.info("lookupSales function started", input=input)

        items = [
            Book1(
                chapter="1",
                part="1",
                content="""
                            The Surprising Power of Atomic Habits
                            THE FATE OF British Cycling changed one day in 2003. The
                            organization, which was the governing body for professional
                            cycling in Great Britain, had recently hired Dave Brailsford as its new
                            performance director. At the time, professional cyclists in Great Britain
                            had endured nearly one hundred years of mediocrity. Since 1908,
                            British riders had won just a single gold medal at the Olympic Games,
                            and they had fared even worse in cycling's biggest race, the Tour de
                            France. In 110 years, no British cyclist had ever won the event.
                            In fact, the performance of British riders had been so
                            underwhelming that one of the top bike manufacturers in Europe
                            refused to sell bikes to the team because they were afraid that it would
                            hurt sales if other professionals saw the Brits using their gear.
                            Brailsford had been hired to put British Cycling on a new trajectory.
                            What made him different from previous coaches was his relentless
                            commitment to a strategy that he referred to as “the aggregation of
                            marginal gains,” which was the philosophy of searching for a tiny
                            margin of improvement in everything you do. Brailsford said, “The
                            whole principle came from the idea that if you broke down everything
                            you could think of that goes into riding a bike, and then improve it by 1
                            percent, you will get a significant increase when you put them all
                            together.”
                            Brailsford and his coaches began by making small adjustments you
                            might expect from a professional cycling team. They redesigned the
                            bike seats to make them more comfortable and rubbed alcohol on the
                            tires for a better grip. They asked riders to wear electrically heated
                            overshorts to maintain ideal muscle temperature while riding and used""",
            )
        ]

        return str(items)
    except Exception as e:
        log.error("lookupSales function failed", error=e)
        raise e
